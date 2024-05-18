# GenshinAutoPlayWindtrace
原神风行迷踪自动挂机辅助（已适配1920*1080分辨率，支持PC端4.6版本简体中文界面）

原项目：
https://github.com/XiaoMiku01/GenshinAutoPlayBalladsofBreeze

懒人包（请使用管理员权限运行main.exe）：
https://pan.baidu.com/s/1MEJxNw-0mIjeRrzuduTlww?pwd=1234
https://wwl.lanzouq.com/iyXjt1z4jeih

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
0.系统输入法调成英文

1.打开游戏，游戏语言设置为简体中文，分辨率1920*1080窗口化，游戏画面贴靠到屏幕左上角（一定要贴紧，否则鼠标点击位置可能出错，暂不支持其他分辨率，可在游戏内使用Alt+Enter快捷键切换全屏/窗口化）

2.走到吉盖克斯面前，ps.不要将程序最小化，否则检测不到游戏界面！！

3.确保游戏画面没有被任何窗口遮挡（否则鼠标键盘操作会输入到最上层应用）

4.以管理员权限运行 main.py。（没有python环境就下载懒人包运行.exe文件，windows系统需要右键-以管理员权限运行！！使用Pycharm之类的IDE运行需要以管理员权限启动Pycharm再运行脚本）
```shell
python3 main.py
```
5.开始自动挂机
![image](游戏窗口贴靠说明.png)
