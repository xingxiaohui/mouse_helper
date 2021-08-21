"""
程序主入口
其他模块都可删除了都以方法的形式写在这里
"""
import os
import random
import time

import pyautogui
import pynput
from mouse_helper import utils
from mouse_helper import config
import json
from tkinter import END
## 监听鼠标
from pynput.mouse import Listener as mouseListener
from pynput.keyboard import Key, Listener as keyListener


def on_click(x, y, button, pressed):
    if pressed:
        global start_time
        now_time = time.time()
        time_take = now_time - start_time
        start_time = now_time
        action_list.append({
            "action": "move",
            "x": x,
            "y": y,
            "time": time_take
        })
        # 监听鼠标点击
        print('{0}'.format(button))
        global count
        count = count + 1
        logger.insert(END, '{0} ： {1}\n'.format('记录鼠标点击', (x, y)))
        if count > 60:
            logger.delete(1.0, END)  # 使用 delete
            logger.insert(END, ' 清空日志\n')
            logger.see(END)


def on_press(key):
    print('{0} 被按下'.format(key))

    if key == Key.f5:
        print('you press f5')
        stop_script()
        mouse_listener.stop()  # 停止监视 鼠标
        return False  # 按键是f5,停止监视 键盘


def on_release(key):
    # 没啥用这里
    if key == Key.enter:
        print('you release Enter')


# 录制脚本
def create_script(app, path, log):
    log.insert(END, '倒计时5秒后开始录制鼠标点击')
    time.sleep(5)
    app.iconify()  # 最小化窗口
    global action_list
    global file_path
    global start_time
    global mouse_listener
    global count
    global logger
    count = 0
    logger = log
    file_path = path
    action_list = []
    start_time = time.time()

    mouse_listener = mouseListener(on_click=on_click)
    mouse_listener.start()
    with keyListener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


# 结束录制
def stop_script():
    data = {
        "steps": action_list
    }
    with open(file_path, 'w+') as f:
        json.dump(data, f)


# 执行脚本
def run_script(app, path, cheat_flag, log):
    log.insert(END, '倒计时5秒后开始执行鼠标点击')
    num = 0
    time.sleep(5)
    app.iconify()  # 最小化窗口
    with open(path, 'r') as f:
        load_data = json.load(f)
        data = load_data.get("steps")
        for i in data:
            num = num + 1
            if i.get("action") == "move":
                pyautogui.moveTo((i.get("x"), i.get("y")), duration=i.get("time"))
                print('cheat_flag')
                print(cheat_flag)
                if cheat_flag == 0:
                    pyautogui.click(clicks=1, interval=0)
                else:
                    cheat_click((i.get("x"), i.get("y")))
                x, y = pyautogui.position()
                log.insert(END, '{0} ： {1}\n'.format('执行鼠标点击', (x, y)))
            if num > 60:
                log.delete(1.0, END)  # 使用 delete
                log.insert(END, ' 清空日志\n')
                log.see(END)


def cheat_pos(origin, factor=5):
    """
    对原始点击坐标进行随机偏移，防止检测
    :param origin:原始坐标
    :param factor:偏移量
    :return new:偏移后的坐标
    """
    if origin is not None:
        x, y = random.randint(-factor, factor), random.randint(-factor, factor)
        new = (origin[0] + x, origin[1] + y)
        return new
    return origin


def cheat_click(target):
    """
    点击屏幕上的某个点
    :param target:目标点
    """
    if target is None:
        print('未检测到目标')
    else:
        pyautogui.moveTo(cheat_pos(target), duration=0.20)
        times = random.randint(1, 2)
        interval_time = random.randint(8, 30)
        pyautogui.click(clicks=times, interval=interval_time / 100)
