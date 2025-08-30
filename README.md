# ComfyUIGradio

ComfyUIGradio は AI を用いて画像や動画の生成等を行う [ComfyUI](https://www.comfy.org/) を
利用して、 [Gradio](https://www.gradio.app/)による独自の簡易ユーザーフェイスを用いて、
イラスト画像生成や動画生成を行うツールです。

- [使い方](https://asfdrwe.github.io/ComfyUIGradio/)

## インストール
```
git clone https://github.com/asfdrwe/ComfyUIGradio
cd ComfyUIGradio
python3.13 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## 実行

```
python app.py
```

### 起動オプション

ComfyUI を別のマシンで動かしている場合、次のオプションで接続できます。

- --server_addr ComfyUIのアドレス
- --server_port ComfyUIのポート番号

```
python app.py --server_addr ComfyUIのアドレス --server_port ComfyUIのポート番号
```

## ライセンス

ComfyUIGradio は MIT LICENSE に従います。

Windows 用配布パッケージに含まれるプログラムやモデルはそれぞれのライセンスに従います。

Copyright (c) 2025 asfdrwe <asfdrwe@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## 使用プログラム・モデル

- [Python](https://www.python.org/)
- [ComfyUI](https://www.comfy.org/) 
- [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF)
- [ComfyUI-DepthAnythingV2](https://github.com/kijai/ComfyUI-DepthAnythingV2)
- [Gradio](https://www.gradio.app/)

- [WAI-NSFW-illustrious-SDXL-v14.0](https://civitai.com/models/827184/wai-nsfw-illustrious-sdxl)
- [DMD2](https://huggingface.co/tianweiy/DMD2)
- [WAINSFW14+DMD2-GGUF](https://huggingface.co/asfdrwe/WAI14DMD2-GGUF)
- [DepthAnythingV2](https://huggingface.co/Kijai/DepthAnythingV2-safetensors/tree/main)
- [CN-anytest_v4-marged](https://huggingface.co/2vXpSwA7/iroiro-lora)
- [Wan2.1_14B_VACE-GGUF](https://huggingface.co/QuantStack/Wan2.1_14B_VACE-GGUF)
- [umt5-xxl-encoder-gguf](https://huggingface.co/city96/umt5-xxl-encoder-gguf)
- [wan_2.1_vae](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged))
- [Wan21_CausVid_14B_T2V_lora_rank32_v1_5_no_first_block](https://huggingface.co/Kijai/WanVideo_comfy)
