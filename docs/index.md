# ComfyUIGradio

ComfyUIGradio は AI を用いて画像や動画の生成等を行う [ComfyUI](https://www.comfy.org/) を
利用して、 [Gradio](https://www.gradio.app/)による独自の簡易ユーザーフェイスを用いて、
イラスト画像生成や動画生成を行うツールです。

操作可能な場所を減らし必要最小限の項目のみ入力するだけで画像や動画を生成できるので、
生成 AI 初心者でも扱いやすいと思います。

AUTOMATIC1111 や Forge 等既存の Gradio ベースの画像生成ツールユーザ向けには、
モデルやLoRA等の細かい指定が可能な[ComfyUIGradio2](https://github.com/asfdrwe/ComfyUIGradio2) を
提供しているのでこちらもご活用ください。

## 動作確認環境

|       OS         |             ハードウェア                            |             備考           |
|------------------|---------------------------------------------------|----------------------------|
| Windows 11 24H2  | Ryzen 5600 + DDR4 3200 16GB×2 + Geforce 3060      |                            |
| Fedora 42 (Linux)| Ryzen 5600G + DDR 3200 16GB×2 + Radeon RX 7800 XT | ComfyUI の起動オプションに工夫が必要 |

画像生成は NVIDIA の VRAM 8GB 以上の以上のグラフィックボードとメインメモリ 16GB あれば
可能だと思います。動画生成は NVIDIA の VRAM 12GB 以上のグラフィックボードと
メインメモリ 32GB 以上ないと困難だと思います。

NVIDIA 以外の環境は基本的に Linux 上で AMD Radeon RX 7800 XT でしか動作確認していません。
(M4 Mac Mini でもWindows 上で動作する ComfyUI へ接続した場合は動作することを確認していますが
Mac 上で ComfyUI を動かした場合は確認していません)。また、Radeon では ComfyUI のオプションを
細かく指定しないとうまく動かないので非推奨です
