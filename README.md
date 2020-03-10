# annotation_assistant

hand annotation assistant

## AIm

Neural Network Console Chalenge https://nnc-challenge.com/
のアノテーション作業をなんとか効率化させたくて作った

## How to

path 変数`data_dir_path`と`csv_path`を書き換えて

    python annotation.py

それ以降はコマンドラインの表示に従ってアノテーションできます
`Ctrl+D`でプログラムを中止できます．
中止後に再度

    python annotation.py

すれば，前回の途中からアノテーションできます

## Post Scripts

作ったはいいけど，自己満足がすぎる
折角プログラミング不要で訓練できるシステムなのに，これだとデータセット作成時にコードを読ませちゃうのでビミョウ感w
