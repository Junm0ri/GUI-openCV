import numpy as np
import PySimpleGUI as sg
import cv2
from pathlib import Path

"""
[Todo]
・保存ボタンを押した時、ウィンドウを表示して画像の保存先を確認したい→cv.imwriteで保存
（Or... sg.saveasという機能があるらしい）

"""

def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None

def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def file_read():
    '''
    ファイルを選択して読み込む
    '''
    fp = ""
    # GUIのレイアウト
    layout = [
        [
            sg.FileBrowse(key="file"),
            sg.Text("ファイル"),
            sg.InputText()
        ],
        [sg.Submit(key="submit"), sg.Cancel("Exit")]
    ]
    # WINDOWの生成
    window = sg.Window("ファイル選択", layout)

    # イベントループ
    while True:
        event, values = window.read(timeout=100)
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        elif event == 'submit':
            if values[0] == "":
                sg.popup("ファイルが入力されていません。")
                event = ""
            else:
                fp = values[0]
                break
    window.close()
    return Path(fp)

class Main:
    def __init__(self):
        # ファイル読み込み
        # self.fp=file_read()
        self.image=imread("C:/Users/yukku/OneDrive/ドキュメント/GitHub/-/Images/input2.png")
        # self.image=imread(self.fp)

        #画像ビューワーの大きさ調整
        self.re_length=480 #リサイズ後の横長さ
        self.h,self.w=self.image.shape[:2] #縦横の辺の長さ
        self.re_h=self.re_w=self.re_length/self.w
        self.image=cv2.resize(self.image,dsize=None,fx=self.re_h,fy=self.re_w)

    def run(self):

        # GUIのレイアウト
        layout=[
           [sg.Image(filename='',key='-IMAGE-')],
           
            [ #ガウシアンフィルタ
                sg.Checkbox("Gaussian",key='-GAUSSIAN-',enable_events=True),
                sg.Slider(
                    (0, 255),
                    1,
                    1,
                    orientation='h', #バーの方向
                    size=(45, 15),
                    key='-Gsigma-', #ガウシアンフィルタのσ（これよりもカーネルサイズを変更できるようにしたほうがいいか？）
                    enable_events=True
                )
            ],
            [ #メディアンフィルタ
                sg.Checkbox("Median",key='-MEDIAN-',size=(7,1),enable_events=True),
                sg.Slider(
                    (1, 9),
                    1,
                    1,
                    orientation='h', #バーの方向
                    size=(45, 15),
                    key='-MKernel-', #ガウシアンフィルタのσ（これよりもカーネルサイズを変更できるようにしたほうがいいか？）
                    enable_events=True
                )
            ],
            [ #Threshold
                sg.Checkbox("Threshold",key='-THRESH-',enable_events=True), #二値化処理（Cannyを使用か）
                sg.Slider(
                    (0, 255),
                    1,
                    1,
                    orientation='h', #バーの方向
                    size=(45, 15),
                    key='-Thre1-', #
                    enable_events=True
                )
            ], 
            [ #Canny
                sg.Checkbox("Canny",key='-CANNY-',enable_events=True), #二値化処理（Cannyを使用か）
                sg.Slider(
                    (0, 255),
                    1,
                    1,
                    orientation='h', #バーの方向
                    size=(22, 15),
                    key='-Canny1-', #
                    enable_events=True
                ),
                sg.Slider(
                    (0, 255),
                    1,
                    1,
                    orientation='h', #バーの方向
                    size=(22, 15),
                    key='-Canny2-', #
                    enable_events=True
                )
            ],
            [
                sg.Submit(button_text='保存',key='Save')
            ]
        ]
        # Windowを生成(Todo:locationの位置をimageの高さだけ上にシフトしたい)
        window = sg.Window('フィルタリング調整', layout, location=(0, 0))
        # window = sg.Window('フィルタリング調整', layout)
        event,values = window.read(timeout=0)

        # メインループ
        try:
            while True:
                
                Image=self.image

                # imgbytes = cv2.imencode('.png', Image)[1].tobytes()
                # window['-IMAGE-'].update(data=imgbytes)
                
                # ガウシアンフィルタ
                if values['-GAUSSIAN-']:
                    Image = cv2.GaussianBlur(Image, (9,9), values['-Gsigma-'])
                    # window['-Gsigma-'].update(values['-Gsigma-'])
                
                if values['-MEDIAN-']:
                    Image = cv2.medianBlur(Image, ksize=3)
                    # print(type(values['-MKernel-']))
                    A=int(values['-MKernel-'])
                    A+=(A+1)%2
                    Image = cv2.medianBlur(Image, ksize=A)


                #Threshold
                if values['-THRESH-']:
                    Image = cv2.cvtColor(Image, cv2.COLOR_BGR2LAB)[:, :, 0]
                    Image = cv2.threshold(Image, values['-Thre1-'], 255, cv2.THRESH_BINARY)[1]

                #Canny
                if values['-CANNY-']:
                    Image = cv2.Canny(Image, values['-Canny1-'], values['-Canny2-'])

                #保存処理
                if event == "Save":
                    sg.popup_yes_no('www')

                # #操作を反映
                imgbytes = cv2.imencode('.png', Image)[1].tobytes()
                window['-IMAGE-'].update(data=imgbytes)

                #操作読み込み（初期状態で画像を表示するために場所を移動した）
                event,values = window.read()

                if event in ('Exit', sg.WIN_CLOSED):
                    # sg.popup_yes_no("終了しますか？")
                    break
                
        finally:
            window.close()

if __name__=='__main__':
    Main().run()