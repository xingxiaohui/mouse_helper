"""
公用方法模块
"""
import random
import time
import cv2
import numpy
import pyautogui
from PIL import ImageGrab
import aircv as ac


# 禁用 pyautogui 的保护性退出
pyautogui.FAILSAFE = False


# 采用封装后的算法来进行识别  效率非常好
def find_and_click(target, factor):
    """
    整合整个流程，找到目标位置偏移后点击
    :param target:目标图片位置
    :return pos:最终点击的位置
    """
    screen = screen_shot()
    target = ac.imread(target)
    confidence = 0.9
    # 获取匹配结果
    match_result = ac.find_template(screen, target, confidence)
    if match_result is not None:
        print(match_result)
        x = match_result['result'][0]
        y = match_result['result'][1]
        # 当前x y为识别图片的中心点，可以进行直接点击
        origin = (x, y)
        # 偏移坐标并点击
        pos = cheat_pos(origin, factor=factor)
        click(pos)
        return pos
    return None


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


def screen_shot():
    """
    获取屏幕截图
    :return:
    """
    screen = ImageGrab.grab()
    screen = cv2.cvtColor(numpy.asarray(screen), 0)
    return screen
