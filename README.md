# GUI-openCV
OpenCVのフィルタリング処理をインタラクティブウィンドウ上で行い、処理後の画像を保存することができるデスクトップアプリです。

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

# 適用例（Threshold）

<img width="268" alt="スクリーンショット 2022-02-02 0117402" src="https://user-images.githubusercontent.com/79455149/152006991-48855e23-4f39-4bee-92b3-1ff78b2058a6.png">
