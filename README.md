# GUI-openCV
PysimpleGUIを利用してOpenCVのフィルタリング処理をインタラクティブウィンドウ上で行い、処理後の画像を保存することができるデスクトップアプリです。

※OpenCV,PySimpleGUIのインストールが必要です

exeファイルを配布する方法は現在模索中です...
（GitHubでは100MBまで、Vectorでは200MBまでという制限があり、実際のサイズは250MB）

# 使い方


![image](https://user-images.githubusercontent.com/79455149/152005322-0790e2bc-10fe-4d7b-b6e9-7bc54775a43d.png)

アプリを起動するとこんな画面が表示されます。Browseボタンを押して端末の画像ファイルを選択→Submitを押してください

<img width="268" alt="スクリーンショット 2022-02-02 0113182" src="https://user-images.githubusercontent.com/79455149/152006285-335ec95f-a10c-4605-a82b-9f32d46c8582.png">

画像を選択するとメイン画面が表示されます。適用したい処理のチェックボックスにチェックを入れて、スライダにより処理の大きさを決定してください。

＜現時点で使用可能な処理＞

・GaussianBlur(ガウシアンフィルタ)

・MedianBlur(メジアンフィルタ)

・Threshold(二値化)

・Canny（エッジ検出）

# 適用例

・Gaussian

<img width="268" alt="Gaussian" src="https://user-images.githubusercontent.com/79455149/152008503-b0a69380-839d-4ba7-9a71-de9dcc9cf406.png">

・Median

<img width="268" alt="Median" src="https://user-images.githubusercontent.com/79455149/152008559-e5abea2f-100c-454a-80f9-a00ee79ea25b.png">

・Threshold

<img width="268" alt="スクリーンショット 2022-02-02 0117402" src="https://user-images.githubusercontent.com/79455149/152006991-48855e23-4f39-4bee-92b3-1ff78b2058a6.png">

・Canny

<img width="268" alt="Canny" src="https://user-images.githubusercontent.com/79455149/152008626-42b78909-0779-4bd9-a0b2-f5804a16ef62.png">
