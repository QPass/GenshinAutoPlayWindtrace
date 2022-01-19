# GenshinAutoPlayWindtrace
原神风行迷踪自动挂机辅助（已适配1920*1080分辨率）

原项目：
https://github.com/XiaoMiku01/GenshinAutoPlayBalladsofBreeze

懒人包：
https://pan.baidu.com/s/1oL7E2-sTQ3tYo5PAwPA1xQ?pwd=yawb

### 语言环境
python3

### 第三方库
PyQt5	(读取屏幕)
```shell
python3 -m pip install PyQt5
```
pyautogui	(键盘输入)
```shell
python3 -m pip install pyautogui
```
cv2		(图像识别)
```shell
python3 -m pip install opencv-python
```

win32gui(以下二选一安装)
```shell
python3 -m pip install win32gui
python3 -m pip install pywin32
```

### 使用方法
0.输入法调成英文

1.打开游戏，分辨率调到1920*1080窗口化，游戏画面贴靠到屏幕左上角（一定要贴紧，否则鼠标点击位置可能出错）

2.走到吉盖克斯面前，ps.不要将程序最小化，否则检测不到游戏界面！！

3.确保游戏画面没有被任何窗口遮挡（否则鼠标键盘操作会输入到最上层应用）

4.运行 main.py。（没有python环境或第三方库就运行exe文件，windows下请右键-以管理员权限运行！！）
```shell
python3 main.py
```
5.开始自动挂机

