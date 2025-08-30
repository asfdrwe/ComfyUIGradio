# SPDX-FileCopyrightText: 2025 asfdrwe <asfdrwe@gmail.com>
# SPDX-License-Identifier: MIT

import gradio as gr

import json
import random
import sys

import comfyutils

server_address = "localhost:8188"

def generate(image, positive, denoise):
    baseimage_name = comfyutils.upload_data(image, server_address)

    prompt_file = open("workflow/image2image.json", "r")
    prompt = json.load(prompt_file)
    prompt["24"]["inputs"]["image"] = baseimage_name

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

    baseimage = gr.Image(label = "画像", type = 'filepath')
    positive = gr.TextArea(label = "ポジティブプロンプト")
    denoise  = gr.Slider(label = "ノイズ強度", value = 0.75, minimum = 0.0, maximum = 1.0)
    image    = gr.Image(label = "生成画像", type = 'filepath')

    app = gr.Interface(
      fn = generate,
      title = "画像と文章から画像生成",
      inputs = [baseimage, positive, denoise],
      outputs = [image],
      submit_btn = "生成",
      clear_btn = None,
    flagging_mode = "never")

    return app



