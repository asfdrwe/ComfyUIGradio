# 使い方

上に7つのタブが用意されています。左の5つが画像生成、右の2つが動画生成です。

![install05.png](image/install05.png)

## 文章から(文章から画像生成)

ポジティブプロンプトに、生成したい画像に関する英単語をコンマ(,)で区切って入力し、
幅と高さに生成したい画像の大きさを指定してください。

プロンプト例:
```
1girl, smile, school uniform, classroom, standing
(少女、笑顔、制服、教室、立っている)
```

![usage01.png](image/usage01.png)

生成ボタンを押せば右の生成画像に画像が生成されます。

![usage02.png](image/usage02.png)

`ComfyUI`フォルダの`output`フォルダに保存されます。

![usage03.png](image/usage03.png)
![generated01.png](generated/ComfyUI_00001_.png)

ComfyUIGradio の生成画像の上で右クリックして名前を付けて保存でも保存できますが、
ファイル名がview(拡張子なし)なので、適当なファイル名＋拡張子『.png』(tmp01.png等)で保存してください。

プロンプトの具体例は『sdxl プロンプト例』等で検索してください(なお画像に含めたくない内容を入力する
ネガティブプロンプトは使えません)。

## 画像から(画像と文章から画像生成)

![usage04.png](image/usage04.png)

左上の画像欄に画像をここにドロップまたはクリックして元となる画像のアップロードを
行ってください。アップロードした画像は `ComfyUI` フォルダの `input` フォルダに
保存されます。ここではさきほど生成した画像を使います。

![usage05.png](image/usage05.png)

この画像に対して、生成したい画像に関する英単語をコンマで区切ってポジティブプロンプトに入力します。
生成ボタンを押せば右の生成画像に画像が生成されます。

プロンプト例:
```
1girl, angry, school uniform, classroom, standing
(少女、怒り、制服、教室、立っている)
```

![usage06.png](image/usage06.png)
![generated02.png](generated/ComfyUI_00002_.png)

ノイズ強度を上げると元の画像から大きく変化し、ノイズ強度を下げると元の画像により
近い画像が生成されます。デフォルトは 0.75 にしています。1 にすると元の画像を
参照しないのと同じになります。

![usage07.png](image/usage07.png)

## 画像の一部修正(画像の一部を文章に基づき修正)

左上の画像欄に一部修正したい画像をここにドロップまたはクリックして元となる画像のアップロードを
行ってください。

![usage08.png](image/usage08.png)

画像に対して修正したい箇所をマウスで塗ってください。左の黒丸でブラシの大きさ、
右上に元に戻すボタン等があります。修正したい内容に関する英単語をコンマで区切って
ポジティブプロンプトに入力します。

プロンプト例:
```
1girl, smile, open mouth, classroom, school uniform, standing
(少女、笑顔、口を開ける、教室、制服、立っている)
```

![usage09.png](image/usage09.png)

生成ボタンを押せば右の生成画像に画像が生成されます。

![usage10.png](image/usage10.png)
![generated03.png](generated/ComfyUI_00003_.png)

ノイズ強度を上げると元の画像から大きく変化し、ノイズ強度を下げると元の画像により
近い画像が生成されます。

うまくいかない場合はノイズ強度を変えて何度も試してみてください。

## 画像の特徴から(画像の特徴と文章から画像生成)
画像の特徴を理解して生成画像に反映できる ControlNet 機能を利用して、落書きレベルの
線画(Scribble)や棒人形で人のポーズを指定できる [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)形式の
画像と、ポジティブプロンプトに入力した文章から画像を生成します。

画面構成やポーズを指定できるので、文字では記述しにくい画像内容でも生成しやすくなります。

線画は適当なペイントツールで自分で描いてください。

OpenPose 形式のポーズ画像は[3D Openpose Editor](https://openposeai.com/)で作成できます。
写実的な人物画像から OpenPose 形式のポーズ画像を生成することも できます。

![usage11.png](image/usage11.png)
![usage12.png](image/usage12.png)

3D Openpose Editor についてはAUTOMATIC1111拡張の解説なので少し違う部分もありますが
[こちら](https://note.com/levelma/n/na348b35d5fa1)などを参考にしてください。

線画やポーズ画像を左上の画像からアップロードしてください。
ここでは次の OpenPose 形式の画像を保存してアップロードしてください。

![pose_2025_08_30_14_48_30.png](image/pose_2025_08_30_14_48_30.png)

生成したい内容に関する英単語をコンマ区切りでポジティブプロンプトに入力します。

プロンプト例:
```
1girl, smile, classroom, school uniform
(少女、笑顔、教室、制服)
```

![usage13.png](image/usage13.png)

生成ボタンを押せば右の生成画像に画像が生成されます。

![usage14.png](image/usage14.png)
![generated04.png](generated/ComfyUI_00004_.png)

うまくいかない場合も多いので何度も生成してください。

## 画像の深度情報から(画像の深度情報と文章から画像生成)

元の画像から深度情報（画像に描かれているものへの距離を濃淡値で表した画像)を抽出し
ControlNet に与え、さらにポジティブプロンプトに入力した文章から画像を生成します。

元の画像の画面構成を反映できるので、文字では記述しにくい画像内容でも生成しやすくなります。

左上の画像から参照元画像をアップロードしてください。
ポジティブプロンプトに内容に関する英単語をコンマで区切って入力します。

プロンプト例:
```
1girl, crying, tears, pink hair, school uniform, short sleeves, 
white shirt, green tie, grey skirt, pleated skirt, plaid skirt
(少女、泣く、涙、ピンク髪、制服、短袖、
白シャツ、緑タイ、グレースカート、プリーツスカート、チェック柄スカート)
```

![usage15.png](image/usage15.png)

生成する画像の幅や高さを指定して生成ボタンを押してください。
画像と深度情報が生成されます。

![usage16.png](image/usage16.png)
![generated05.png](generated/ComfyUI_00006_.png)
![depth01.png](generated/Depth_00001_.png)

## 画像から動画(画像と文章から動画生成(Wan2.1))

Wan2.1 Vace を利用して開始画像を指定し、その画像に対する生成したい動画に関する文章を
英文(または中国語文)で入力することで、動画を生成することができます。

左上の画像から開始画像をアップロードしてください。

ポジティブプロンプトは、これまでと異なり、英語(または中国語)の文章で入力します。
幅と高さとフレーム数を指定してください。フレーム数は動画の長さです。
1 秒 16 フレームなので、17 フレームで約 1 秒、33 フレームで約 2 秒、49 フレームで
約 3 秒となります。ここでは横:480 縦:640 時間:49 フレーム 約 3 秒で の動画を生成します。

プロンプト例:
```
A girl is dancing intensively in classroom.
(少女が教室で激しく踊っている)
```

![usage17.png](image/usage17.png)

生成ボタンを押して動画を生成してください。画像に比べると生成には時間がかかります。

![usage18.png](image/usage18.png)
![type:video](generated/ComfyUI_00008_.webm)

webm 形式の動画は標準ではブラウザで再生できるので、保存した動画ファイルを再生したい場合は
ブラウザにドラックアンドドロップしてください。

## 画像と動画から動画(画像と動画の特徴と文章から動画生成(Wan2.1))

開始画像と参照動画の深度情報に基づく動きと動作に関する文章から動画を生成することができます。

左上の画像から開始画像をアップロードしてください。

参照動画の例として
[ComfyUI の wiki](https://docs.comfy.org/tutorials/video/wan/vace)より
[この動画](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/video/wan/vace/v2v/vace_v2v.mp4)をダウンロードしてください。

ポジティブプロンプトは英文で入力します。
幅と高さとフレーム数を指定してください。ここでは横:480 縦:640 時間:49 フレーム 約 3 秒で の動画を生成します。

プロンプト例: 
```
A girl is dancing in classroom.
(少女が教室で踊っている)
```

![usage19.png](image/usage19.png)
![usage20.png](image/usage20.png)

生成ボタンを押して動画を生成してください。

![type:video](generated/ComfyUI_00010_.webm)
![type:video](generated/Depth_00002_.webm)

## 動作がおかしい場合

Gradio でファイルを扱う際のファイルのキャッシュは Windows の場合標準では
`C:\ユーザ\ユーザ名\AppData\Local\gradio` です。

ComfyUI の出力と ComfyUIGradio の生成時の表示が食い違うなど、動作が
おかしくなっている場合、このフォルダを削除し、ブラウザのキャッシュを
削除し、ComfyUI と ComfyUIGradio を再起動してください。

