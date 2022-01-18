import win32gui
from PyQt5.QtWidgets import QApplication
import sys
import cv2
import pyautogui as pg
from merge import manyimgs
import numpy as np
import time

hwnd_title = dict()

c = ''
gamestate = 0


# 均值哈希算法
def aHash(img):
    # 缩放为8*8
    img = cv2.resize(img, (8, 8))
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # s为像素和初值为0，hash_str为hash值初值为''
    s = 0
    hash_str = ''
    # 遍历累加求像素和
    for i in range(8):
        for j in range(8):
            s = s + gray[i, j]
    # 求平均灰度
    avg = s / 64
    # 灰度大于平均值为1相反为0生成图片的hash值
    for i in range(8):
        for j in range(8):
            if gray[i, j] > avg:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str


# Hash值对比 返回值（正整数）越小相似度越高
def cmpHash(hash1, hash2):
    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1) != len(hash2):
        return -1
    # 遍历判断
    for i in range(len(hash1)):
        # 不相等则n计数+1，n最终为相似度
        if hash1[i] != hash2[i]:
            n = n + 1
    return n


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)
for h, t in hwnd_title.items():
    if t == "原神":
        hwnd = h
        break

imgF = cv2.imread('./image/F.png')
imgF2 = cv2.imread('./image/F2.png')
imgMatchgame = cv2.imread('./image/Matchgame.png')
imgAcceptgame = cv2.imread('./image/Acceptgame.png')
imgReady = cv2.imread('./image/Ready.png')
imgSpace = cv2.imread('./image/Space.png')
imgFull = cv2.imread('./image/Full.png')
imgQ = cv2.imread('./image/Q.png')  # 1808,1028   23,24
imgE = cv2.imread('./image/E.png')  # 1678,1029  27,21
imgPlayer1P = cv2.imread('./image/1P.png')  # 349,30    32,28
imgQuit1 = cv2.imread('./image/Quit1.png')  # 1494,995  279,45
imgQuit2 = cv2.imread('./image/Quit2.png')  # 876,277  170,46

hashF = aHash(imgF)
hashF2 = aHash(imgF2)
hashMatchgame = aHash(imgMatchgame)
hashAcceptgame = aHash(imgAcceptgame)
hashReady = aHash(imgReady)
hashSpace = aHash(imgSpace)
hashFull = aHash(imgFull)
hashQ = aHash(imgQ)
hashE = aHash(imgE)
hashPlayer1P = aHash(imgPlayer1P)
hashQuit1 = aHash(imgQuit1)
hashQuit2 = aHash(imgQuit2)

app = QApplication(sys.argv)

print("请以管理员身份运行本程序")
print("请将游戏窗口化，1920x1080分辨率，窗口贴靠在屏幕左上角")
print("请走到吉盖克斯身边,让【F吉盖克斯】对话框出现在画面中")
print("请确保游戏画面没有被任何窗口遮挡，程序将在5秒后启动")
time.sleep(5)
win32gui.SetForegroundWindow(hwnd)
while 1:
    screen = QApplication.primaryScreen()  # 抓取屏幕
    abc = screen.grabWindow(hwnd).toImage()
    s = abc.bits().asstring(abc.width() * abc.height() * abc.depth() // 8)
    img1 = np.frombuffer(s, dtype=np.uint8).reshape((abc.height(), abc.width(), abc.depth() // 8))
    F = img1[525:525 + 29, 1101:1101 + 36]  # F 对话框 吉盖克斯 36*29
    F2 = img1[488:488 + 31, 1100:1100 + 37]  # F 对话框 吉盖克斯+坐下
    posiplay1 = [1433, 578]  # 鼠标点击 对话框 游玩 风行迷踪
    Matchgame = img1[991:991 + 52, 1211:1211 + 644]  # 按钮 匹配游戏
    Acceptgame = img1[711:711 + 52, 1000:1000 + 325]  # 按钮 接受
    Ready = img1[994:994 + 48, 1539:1539 + 328]  # 按钮 准备就绪
    Space = img1[1028:1028 + 23, 1661:1661 + 62]  # 按键提示图标 空格
    Full = img1[476:476 + 77, 545:545 + 824]  # 提示框 达到上限
    Q = img1[1028:1028 + 24, 1808:1808 + 23]  # 元素爆发提示
    E = img1[1029:1029 + 21, 1678:1678 + 27]  # 元素战技提示
    Player1P = img1[30:30 + 28, 349:349 + 32]  # 联机模式提示
    Quit1 = img1[995:995 + 45, 1494:1494 + 279]  # 回到单人模式按钮
    Quit2 = img1[277:277 + 46, 876:876 + 170]  # 解散队伍按钮

    w, a, s, d = img1[395:395 + 180, 395:395 + 180], img1[557:557 + 180, 227:227 + 180], img1[722:722 + 180,
                                                                                         393:393 + 180], img1[
                                                                                                         557:557 + 180,
                                                                                                         563:563 + 180]
    i, j, k, l = img1[395:395 + 180, 1343:1343 + 180], img1[557:557 + 180, 1180:1180 + 180], img1[722:722 + 180,
                                                                                             1343:1343 + 180], img1[
                                                                                                               557:557 + 180,

                                                                                                               1513:1513 + 180]

    try:
        imgs = manyimgs(1, ([w, a], [s, d], [i, j], [k, l]))
    except Exception:
        print('程序出错！请确保原神在前台，不要最小化!')
        break

    if cmpHash(hashQ, aHash(Q)) == 0 and cmpHash(hashE, aHash(E)) == 0 and cmpHash(hashPlayer1P, aHash(Player1P)) == 0:
        gamestate = 2  # 可能卡在多人模式
        print("尝试退出多人模式")
        time.sleep(2)
        pg.press("f2")
        time.sleep(3)
        pg.click(1656, 1043)
        time.sleep(2)
        pg.click(1184, 781)
        time.sleep(5)
    elif cmpHash(hashF, aHash(F)) == 0 or cmpHash(hashF2, aHash(F2)) == 0:
        time.sleep(0.5)
        pg.press("f")
        print("尝试与NPC对话")
        time.sleep(3)
        pg.click(1356, 582 + 26)
        gamestate = 0
        print("鼠标点击 游玩风行迷踪")
    elif cmpHash(hashFull, aHash(Full)) == 0:
        print("迷踪币已达上限，程序停止运行")
        break
    elif cmpHash(hashMatchgame, aHash(Matchgame)) == 0:
        time.sleep(0.5)
        pg.click(1550, 1018 + 26)
        print("鼠标点击 匹配游戏")

    elif cmpHash(hashAcceptgame, aHash(Acceptgame)) == 0:
        time.sleep(0.5)
        pg.click(1180, 734 + 26)
        print("鼠标点击 接受")

    elif cmpHash(hashReady, aHash(Ready)) == 0:
        time.sleep(0.5)
        pg.click(1720, 1017 + 26)
        gamestate = 1
        print("鼠标点击 准备就绪")

    elif gamestate == 1 and cmpHash(hashSpace, aHash(Space)) == 0:
        time.sleep(3)
        print("开始游戏")
        pg.keyDown("w")
        time.sleep(5)
        pg.keyUp("w")
        pg.keyDown("a")
        time.sleep(5)
        pg.keyUp("a")
        time.sleep(0.5)
        pg.press("x")
        time.sleep(1)
        pg.press("e")
        gamestate = 0
        print("结束动作")
    elif gamestate == 2 and cmpHash(hashQuit1, aHash(Quit1)) == 0:
        time.sleep(1)
        print("尝试踢出非正常留存的玩家")
        pg.click(1656, 1043)
    elif gamestate == 2 and cmpHash(hashQuit2, aHash(Quit2)) == 0:
        time.sleep(1)
        print("尝试解散队伍")
        pg.click(1184, 781)

    else:
        print("当前画面没有匹配目标")

    time.sleep(2)

cv2.destroyAllWindows()
input('已停止，请重启程序')
