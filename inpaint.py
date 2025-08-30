# SPDX-FileCopyrightText: 2025 asfdrwe <asfdrwe@gmail.com>
# SPDX-License-Identifier: MIT

import gradio as gr

import json
import random
import sys

import comfyutils

server_address = "localhost:8188"

def generate(image, positive, denoise):
    urllist = comfyutils.upload_imagewithmask(image, server_address)
    baseimage_name = urllist[0]
    maskimage_name = urllist[1]

    prompt_file = open("workflow/inpaint.json", "r")
    prompt = json.load(prompt_file)
    prompt["28"]["inputs"]["image"] = baseimage_name
    prompt["29"]["inputs"]["image"] = maskimage_name

    prompt["6"]["inputs"]["text"] = positive
    prompt["7"]["inputs"]["text"] = ""

    prompt["3"]["inputs"]["seed"] = random.randint(0, sys.maxsize)
    prompt["3"]["inputs"]["denoise"] = str(denoise)

    print("SERVER: " + server_address)

    image = comfyutils.get_image(prompt, server_address)

    return image

def create(addr):
    global server_address
    server_address = addr

#    baseimage = gr.ImageEditor(label = "画像", type = 'pil', brush = gr.Brush(colors = "black"), image_mode = 'RGBA')
    baseimage = gr.ImageEditor(label = "画像", type = 'pil', brush = gr.Brush(colors = "white"), image_mode = 'RGBA')

    positive = gr.TextArea(label = "ポジティブプロンプト")
    denoise  = gr.Slider(label = "ノイズ強度", value = 0.6, minimum = 0.0, maximum = 1.0)
    image    = gr.Image(label = "生成画像", type = 'filepath')

    app = gr.Interface(
      fn = generate,
      title = "画像の一部を文章に基づき修正",
      inputs = [baseimage, positive, denoise],
      outputs = "image",
      submit_btn = "修正",
      clear_btn = None,
    flagging_mode = "never")

    return app
