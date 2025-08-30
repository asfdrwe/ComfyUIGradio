# SPDX-FileCopyrightText: 2025 asfdrwe <asfdrwe@gmail.com>
# SPDX-License-Identifier: MIT

import urllib.request
import urllib.parse
import json
import os

import websocket
import uuid

from requests_toolbelt.multipart.encoder import MultipartEncoder
from PIL import Image
import io
from datetime import datetime

import gradio as gr

def queue_prompt(prompt, server_address, client_id):
    p = {'prompt': prompt, 'client_id': client_id}
    data = json.dumps(p).encode('utf-8')
    request =  urllib.request.Request("http://{}/prompt".format(server_address), data=data)
    return json.loads(urllib.request.urlopen(request).read())

def get_history(prompt_id, server_address):
    with urllib.request.urlopen("http://{}/history/{}".format(server_address, prompt_id)) as response:
        return json.loads(response.read())

def get_image(prompt, server_address, progress = None, progress_data = None):
    client_id = str(uuid.uuid4())

    if progress != None:
        progress(0.0, desc='開始')

    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))

    prompt_id = queue_prompt(prompt, server_address, client_id)['prompt_id']
    while True:
        out = ws.recv()
        if isinstance(out, str):
            message = json.loads(out)
            if message['type'] == 'executing':
                print(message)
                data = message['data']
                if progress != None:
                    for key in progress_data:
                        if data['node'] == key:
                            print(progress_data[data['node']])
                            progress(progress_data[data['node']])
                if data['node'] is None and data['prompt_id'] == prompt_id:
                    if progress != None:
                        progress(1.0, desc='終了')
                    break #Execution is done
        else:
            continue
    ws.close()

    history = get_history(prompt_id, server_address)[prompt_id]
    for node_id in history['outputs']:
        node_output = history['outputs'][node_id]
        print(node_output)
        if 'images' in node_output:
            for image in node_output['images']:
                data = {'filename': image['filename'], 'subfolder': image['subfolder'], 'type': image['type']}
                url_values = urllib.parse.urlencode(data)
                image_url = "http://{}/view?{}".format(server_address, url_values)
                print('OUTPUT: ' + image_url)
                return image_url
        return None

def get_images(prompt, server_address, progress = None, progress_data = None):
    client_id = str(uuid.uuid4())

    if progress != None:
        progress(0.0, desc='開始')

    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))

    prompt_id = queue_prompt(prompt, server_address, client_id)['prompt_id']
    while True:
        out = ws.recv()
        if isinstance(out, str):
            message = json.loads(out)
            if message['type'] == 'executing':
                print(message)
                data = message['data']
                if progress != None:
                    for key in progress_data:
                        if data['node'] == key:
                            print(progress_data[data['node']])
                            progress(progress_data[data['node']])
                if data['node'] is None and data['prompt_id'] == prompt_id:
                    if progress != None:
                        progress(1.0, desc='終了')
                    break #Execution is done
        else:
            continue
    ws.close()

    history = get_history(prompt_id, server_address)[prompt_id]
    images_output = []
    for node_id in history['outputs']:
        node_output = history['outputs'][node_id]
        print(node_output)
        if 'images' in node_output:
            for image in node_output['images']:
                 data = {'filename': image['filename'], 'subfolder': image['subfolder'], 'type': image['type']}
                 url_values = urllib.parse.urlencode(data)
                 image_url = "http://{}/view?{}".format(server_address, url_values)
                 print('OUTPUT URL: ' + image_url)
                 images_output.append(image_url)

    return images_output

def upload_data(data_path, server_address, image_type="input", overwrite=False):
    name = os.path.basename(data_path)
    print('UPLOAD: ' + name + ' from ' + data_path)
    with open(data_path, 'rb') as file:
      multipart_data = MultipartEncoder(
        fields= {
          'image': (name, file.read(), 'image/png'),
          'type': image_type,
          'overwrite': str(overwrite).lower()
        }
      )

    data = multipart_data
    headers = { 'Content-Type': multipart_data.content_type }
    request = urllib.request.Request("http://{}/upload/image".format(server_address), data=data, headers=headers)
    with urllib.request.urlopen(request) as response:
      res = response.read()
    res = json.loads(res)
    print('UPLOADED: ' + res['name'])
    return res['name']

def upload_imagewithmask_to_comfy(pil, name, server_address, image_type='input', overwrite=False):
    urllist = []
    img_bytes = io.BytesIO()
    pil['background'].save(img_bytes, format = 'PNG')
    img_bytes = img_bytes.getvalue()
    multipart_data = MultipartEncoder(
      fields= {
        'image': (name, img_bytes, 'image/png'),
        'type': image_type,
        'overwrite': str(overwrite).lower()
      }
    )

    data = multipart_data
    headers = { 'Content-Type': multipart_data.content_type }
    request = urllib.request.Request("http://{}/upload/image".format(server_address), data=data, headers=headers)
    with urllib.request.urlopen(request) as response:
      urllist.append(json.loads(response.read())['name'])

    img_bytes = io.BytesIO()
    pil['layers'][0].save(img_bytes, format = 'PNG')
    img_bytes = img_bytes.getvalue()
    multipart_data = MultipartEncoder(
      fields= {
        'image': ('MASK' + name, img_bytes, 'image/png'),
        'type': image_type,
        'overwrite': str(overwrite).lower()
      }
    )

    data = multipart_data
    headers = { 'Content-Type': multipart_data.content_type }
    request = urllib.request.Request("http://{}/upload/image".format(server_address), data=data, headers=headers)
    with urllib.request.urlopen(request) as response:
      urllist.append(json.loads(response.read())['name'])
    return urllist

def upload_imagewithmask(image, server_address):
    filename = datetime.now().strftime("%Y%m%d.png")
    urllist = upload_imagewithmask_to_comfy(image, filename, server_address)
    print(urllist)
    return urllist

def get_checkpoint(server_address):
    request =  urllib.request.Request("http://{}/models/checkpoints".format(server_address))
    return json.loads(urllib.request.urlopen(request).read())

def get_unetgguf(server_address):
    request =  urllib.request.Request("http://{}/object_info/UnetLoaderGGUF".format(server_address))
    data = json.loads(urllib.request.urlopen(request).read())
    print(data)
    return data['UnetLoaderGGUF']['input']['required']['unet_name'][0]

def get_clipgguf(server_address):
    request =  urllib.request.Request("http://{}/object_info/CLIPLoaderGGUF".format(server_address))
    data = json.loads(urllib.request.urlopen(request).read())
    print(data)
    return data['CLIPLoaderGGUF']['input']['required']['clip_name'][0]

def get_vae(server_address):
    request =  urllib.request.Request("http://{}/models/vae".format(server_address))
    return json.loads(urllib.request.urlopen(request).read())

def get_lora(server_address):
    request =  urllib.request.Request("http://{}/models/loras".format(server_address))
    return json.loads(urllib.request.urlopen(request).read())

def get_sampler(server_address):
    request =  urllib.request.Request("http://{}/object_info/KSampler".format(server_address))
    data = json.loads(urllib.request.urlopen(request).read())
    sampler_list = data['KSampler']['input']['required']['sampler_name'][0]
    print(sampler_list)
    return sampler_list

def get_scheduler(server_address):
    request =  urllib.request.Request("http://{}/object_info/KSampler".format(server_address))
    data = json.loads(urllib.request.urlopen(request).read())
    scheduler_list = data['KSampler']['input']['required']['scheduler'][0]
    print(scheduler_list)
    return scheduler_list

