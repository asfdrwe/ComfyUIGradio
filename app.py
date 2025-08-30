# SPDX-FileCopyrightText: 2025 asfdrwe <asfdrwe@gmail.com>
# SPDX-License-Identifier: MIT

import gradio as gr
import argparse
import sys
import os

base_path = os.path.dirname(os.path.realpath(__file__))
print(base_path)
sys.path.append(os.path.join(base_path, '.'))
print(base_path)

from gradio.processing_utils import PUBLIC_HOSTNAME_WHITELIST

import text2image, image2image, inpaint, controlnet, controlnetdepth
import WanVACEI2V, WanVACEIV2V

server_address = ""

def main():
    parser = argparse.ArgumentParser(description="ComfyUIGradio: WebUI frontend for ComfyUI")
    parser.add_argument('--no-autolaunch', help="not autolaunch web browser", action='store_false')
#    parser.add_argument('--addr', help="server name (default: 127.0.0.1)", default="127.0.0.1")
#    parser.add_argument('--port', help="server port (default: 7860)", default=7860)
    parser.add_argument('--server_addr', help="ComfyUI server URL (default: localhost)", default="localhost")
    parser.add_argument('--server_port', help="ComfyUI server URL (default: 8188)", default="8188")

    args = parser.parse_args()
    server_address = args.server_addr + ":" + args.server_port;
    print(server_address)
    PUBLIC_HOSTNAME_WHITELIST.append(args.server_addr)

    t2i = text2image.create(server_address)
    i2i = image2image.create(server_address)
    inp = inpaint.create(server_address)
    ctn = controlnet.create(server_address)
    ctd = controlnetdepth.create(server_address)
    wiv = WanVACEI2V.create(server_address)
    wvv = WanVACEIV2V.create(server_address)

    app = gr.TabbedInterface(
      [t2i, i2i, inp, 
       ctn, ctd, 
       wiv, wvv], 
      ["文章から", "画像から", "画像の一部修正", 
       "画像の特徴から", "画像の深度情報から", 
       "画像から動画", "画像と動画から動画"])

    app.launch(inbrowser=args.no_autolaunch,
#                server_name=args.addr,
#                server_port=int(args.port),
    )

if __name__  == "__main__":
    main()
