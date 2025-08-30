# SPDX-FileCopyrightText: 2025 asfdrwe <asfdrwe@gmail.com>
# SPDX-License-Identifier: MIT

import gradio as gr

import json
import random
import sys

import comfyutils

server_address = "localhost:8188"

def generate(image, video, positive, width, height, length):
    baseimage_name = comfyutils.upload_data(image, server_address)
    basevideo_name = comfyutils.upload_data(video, server_address)

    prompt_file = open("workflow/WanVACEIV2V.json", "r")
    prompt = json.load(prompt_file)
    prompt["85"]["inputs"]["image"] = baseimage_name

    prompt["6"]["inputs"]["text"] = positive

    prompt["3"]["inputs"]["seed"] = random.randint(0, sys.maxsize)
    prompt["83"]["inputs"]["width"] = width
    prompt["83"]["inputs"]["height"] = height
    prompt["83"]["inputs"]["length"] = length

    print("SERVER: " + server_address)

    videos = comfyutils.get_images(prompt, server_address)

    return videos

def create(addr):
    global server_address
    server_address = addr

    baseimage = gr.Image(label = "画像", type = 'filepath')
    basevideo = gr.Video(label = "参照動画")
    positive  = gr.TextArea(label = "ポジティブプロンプト")
    width     = gr.Number(label = "幅", step = 16, value = 480)
    height    = gr.Number(label = "高さ", step = 16, value = 640)
    length    = gr.Number(label = "フレーム数(fps=16)", minimum = 1, maximum = 161, value 
= 17, step = 16)
    depthvideo = gr.Video(label = "深度動画", autoplay = True, loop = True)
    video     = gr.Video(label = "生成動画", autoplay = True, loop = True)

    app = gr.Interface(
      fn = generate,
      title = "画像と動画の特徴と文章から動画生成(Wan2.1)",
      inputs = [baseimage, basevideo, positive, width, height, length],
      outputs = [depthvideo, video],
      submit_btn = "生成",
      clear_btn = None,
    flagging_mode = "never")

    return app



