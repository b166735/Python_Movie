# Python_Movie
画像処理　課題2

python_2.py:

6,7行目は何もしない関数を定義している。

9行目は表示するウィンドウの名前を"camera"としている。

10から14行目はそれぞれトラックバーの名前、表示先ウィンドウ、最小値、最大値を決めている。

16から18行目で使用するカメラと出力するウィンドウのサイズを決定している。

20から64行目のループでカメラ入力から処理、出力をしている。21行目でカメラ入力した画像を受け取っている。23から27行目でトラックバーから値を受け取っている。28から30行目ではラプラシアンフィルタを定義している。31行目では取得画像のグレースケールを生成している。34から39行目ではカラー画像をそれぞれの成分に分け、0から1の輝度値の範囲に整値している。41から43行目でそれぞれの画像にトラックバーの値vによるガンマ変換を施している。45から50行目ではトラックバーr,g,bの値でそれぞれのカラー画像にガンマ変換をしている。52から55行目ではトラックバーswが1の時、グレースケール画像にラプラシアンフィルタをかけている。swが0の時は3枚に分けたそれぞれのR,G,B成分の画像を1枚のカラー画像に戻している。


使用方法:

1,ソースコードを実行

2,パラメータ変更

  gamma:コントラストの変調
  
  R:R成分の強調
  
  G:G成分の強調
  
  B:B成分の強調
  
  ON/OFF:フィルタを使用するかのオンオフ
  
 3,'q'キーを入力して終了
 

 ![Output sample]() 
