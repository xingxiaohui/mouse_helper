import random

from pynput.mouse import Button, Controller

mouse = Controller()
# print('The current pointer position is {0}'.format(mouse.position))
# 设置鼠标坐标
# mouse.position = (10, 20)
# print('Now we have moved it to {0}'.format(mouse.position))
# 移动鼠标到相对位置
# mouse.move(5, -5)
# # 按住和放开鼠标
# mouse.press(Button.left)  # 按住鼠标左键
# mouse.release(Button.left)  # 放开鼠标左键
# # 点击鼠标
# mouse.click(Button.left, 2)  # 点击鼠标2下
# # 鼠标滚轮
# mouse.scroll(0, 2)  # 滚动鼠标

## 监听鼠标
# from pynput.mouse import Listener as Listener
# from pynput.keyboard import Key, Listener as keyListener
#
#
# def on_click(x, y, button, pressed):
#     # 监听鼠标点击
#     print('{0}'.format(button))
#     print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
#
#
# def on_press(key):
#     print('{0} 被按下'.format(key))
#
#     if key == Key.enter:
#         print('you press Enter')
#         return False  # 按键不是enter,停止监视
#
#
# def on_release(key):
#     if key == Key.enter:
#         print('you release Enter')
#
# # 监听键盘按键
# with keyListener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
# # 连接事件以及释放
# with Listener(on_click=on_click) as listener:
#     listener.join()


# 一个鼠标监听器是一个线程。线程，所有的回调将从线程调用。从任何地方调用pynput.mouse.Listener.stop，或者调用pynput.mouse.Listener.StopException或从回调中返回False来停止监听器。

# 开始时需要记录一个系统时间 start_time 记录鼠标初始位置 start_postion







# import json
# import random
# import time
# import pyautogui
#
#
# list = []
# list.append({
#             "action": "move",
#             "x": 550,
#             "y": 580,
#             "time": 1
#         })
# list.append({
#             "action": "move",
#             "x": 550,
#             "y": 750,
#             "time": 3
#         })
#
# data = {
#     "steps": list
# }
# with open('data.json', 'w') as f:
#     json.dump(data, f)
# with open('data.json', 'r') as f:
#     load_data = json.load(f)
#     data = load_data.get("steps")
#     for i in data:
#         if i.get("action") == "move":
#             pyautogui.moveTo((i.get("x"), i.get("y")), duration=i.get("time"))
#             pyautogui.click(clicks=1, interval=0)
#         if i.get("action") == "click":
#             pyautogui.moveTo((i.get("x"), i.get("y")), duration=i.get("time"))
#             pyautogui.click(clicks=1, interval=0)
#

interval_time = random.randint(8, 30)
print(interval_time/100)