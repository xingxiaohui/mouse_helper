
import random
import time
import pyautogui


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
        interval_time = random.randint(8, 30)
        pyautogui.click(clicks=times, interval=interval_time/100)