# SPDX-FileCopyrightText: 2025 asfdrwe <asfdrwe@gmail.com>
# SPDX-License-Identifier: MIT

import gradio as gr

import json
import random
import sys

import comfyutils

server_address = "localhost:8188"

def generate(image, positive, width, height):
    baseimage_name = comfyutils.upload_data(image, server_address)

    prompt_file = open("workflow/controlnetdepth.json", "r")
    prompt = json.load(prompt_file)
    prompt["24"]["inputs"]["image"] = baseimage_name

    prompt["6"]["inputs"]["text"] = positive
    prompt["7"]["inputs"]["text"] = ""

    prompt["3"]["inputs"]["seed"] = random.randint(0, sys.maxsize)
    prompt["5"]["inputs"]["width"] = width
    prompt["5"]["inputs"]["height"] = height

    print("SERVER: " + server_address)

    images = comfyutils.get_images(prompt, server_address)

    return images

def create(addr):
    global server_address
    server_address = addr

    baseimage = gr.Image(label = "画像", type = 'filepath')
    positive = gr.TextArea(label = "ポジティブプロンプト")
    width    = gr.Number(label = "幅", step = 8, value = 1024)
    height   = gr.Number(label = "高さ", step = 8, value = 1024)

    gallery  = gr.Gallery(label = "生成画像", object_fit = 'scale-down')

    app = gr.Interface(
      fn = generate,
      title = "画像の深度情報と文章から画像生成",
      inputs = [baseimage, positive, width, height],
      outputs = [gallery],
      submit_btn = "生成",
      clear_btn = None,
    flagging_mode = "never")

    return app



