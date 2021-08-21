"""
公用方法模块
原参考的检测算法SIFT在新版本的opencv中被移除了，采用封装了SIFT算法的模块 aircv
模块参考：
https://github.com/NetEaseGame/aircv
方法参考
https://blog.csdn.net/qq_35741999/article/details/100434284
"""
import random
import time
import pyautogui
from PIL import ImageGrab


# 禁用 pyautogui 的保护性退出
pyautogui.FAILSAFE = False


def cheat_pos(origin, factor=5):
    """
    对原始点击坐标进行随机偏移，防止封号
    :param origin:原始坐标
    :param factor:偏移量
    :return new:偏移后的坐标
    """
    if origin is not None:
        x, y = random.randint(-factor, factor), random.randint(-factor, factor)
        new = (origin[0] + x, origin[1] + y)
        return new
    return origin


def click(target):
    """
    点击屏幕上的某个点
    :param target:目标点
    """
    if target is None:
        print('未检测到目标')
    else:
        pyautogui.moveTo(target, duration=0.20)
        times = random.randint(1, 2)
        pyautogui.click(clicks=times, interval=0.25)
        time.sleep(random.randint(500, 1000) / 1000)