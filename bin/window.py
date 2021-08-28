import sys

# 被引用模块所在的路径
import time

sys.path.append("d:/WorkSpace/GitProjects/mouse_helper")

from mouse_helper.thread_initiator import ThreadInitiator
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

# 导入消息对话框子模块
import tkinter.filedialog

tasks = []


# 新建脚本
def create_script(app, log):
    target = "create_script"
    # 获取文件路径
    file_path = tkinter.filedialog.asksaveasfilename()  # 选择保存文件路径
    if ".json" not in file_path:
        messagebox.showwarning('警告', '请创建正确的json文件')
        log.insert(END, 'json脚本文件创建有误请重新创建 **.json 来存储\n')
        return
    threadInitiator = ThreadInitiator(app, target, file_path, log, 0, 0, 1)
    threadInitiator.start()    # 开启新线程
    tasks.append(threadInitiator)    # 记录在运行的线程


# 运行脚本
def run_script(app, loop_flag, cheat_flag, min_flag, log):
    target = "run_script"
    # 获取文件路径
    file_path = tkinter.filedialog.askopenfilename()
    if ".json" not in file_path:
        messagebox.showwarning('警告', '请选择正确的json文件')
        log.insert(END, 'json脚本文件选择有误请重新选择 **.json 来运行\n')
        return
    print(file_path)
    # 创建新线程
    threadInitiator = ThreadInitiator(app, target, file_path, log, loop_flag.get(), cheat_flag.get(), min_flag.get())
    # 开启新线程
    threadInitiator.start()
    # 记录在运行的线程
    tasks.append(threadInitiator)


# 运行截图点击
def image_click(app, loop_flag, cheat_flag, min_flag, log):
    target = "image_click"
    # 获取文件路径
    file_path = tkinter.filedialog.askdirectory()
    if len(file_path) == 0:
        messagebox.showwarning('警告', '请选择正确的文件夹')
        log.insert(END, '文件夹选择有误请重新选择运行\n')
        return
    # 创建新线程
    threadInitiator = ThreadInitiator(app, target, file_path, log, loop_flag.get(), cheat_flag.get(), min_flag.get())
    # 开启新线程
    threadInitiator.start()
    # 记录在运行的线程
    tasks.append(threadInitiator)


def stop():
    global tasks
    for task in tasks:
        task.stop()
    tasks = []


def short_cut(event):
    """
    按f4 停止脚本
    """
    # F4停止
    global app
    if event.keycode == 115:
        stop()


class Window:

    def __init__(self):
        self.app = tk.Tk()  # 根窗口的实例(root窗口)
        self.init_widgets()

    def init_widgets(self):
        # 循环执行
        self.loop_flag = IntVar()
        # 开启随机偏移
        self.cheat_flag = IntVar()
        # 运行时最小化
        self.min_flag = IntVar()
        self.app.title('模拟鼠标助手 V 1.0')
        self.app.geometry('600x300')
        self.app.resizable(0, 0)  # 阻止Python GUI的大小调整
        frame1 = Frame(self.app, padx=20)
        frame1.pack(side=LEFT, fill=BOTH)
        t1 = tk.Label(frame1, text='模拟鼠标助手', font=("华文行楷", 22), borderwidth=2).pack(side=TOP, fill=X, expand=YES)

        frame2 = Frame(self.app)
        t1 = tk.Label(frame2, text='日志', borderwidth=2, font=('微软雅黑', 10), height=1).pack(side=TOP, fill=X, expand=YES)
        t3 = scrolledtext.ScrolledText(frame2, font=('微软雅黑', 10))
        t3.pack(side=TOP, fill=X, expand=YES)
        frame2.pack(side=RIGHT, fill=BOTH, expand=YES)
        Button(frame1, command=lambda: create_script(self.app, log=t3), text='创建脚本', width=20).pack(
            side=TOP, expand=YES)
        Button(frame1, command=lambda: run_script(self.app, self.loop_flag, self.cheat_flag, self.min_flag, log=t3), text='运行脚本', width = 20).pack(
            side=TOP, expand=YES)
        Button(frame1, command=lambda: image_click(self.app, self.loop_flag, self.cheat_flag, self.min_flag, log=t3), text='运行截图点击', width=20).pack(
            side=TOP, expand=YES)
        Checkbutton(frame1, text='循环执行', variable=self.loop_flag, onvalue=1, offvalue=0).pack(side=TOP, anchor='w')
        Checkbutton(frame1, text='随机偏移', variable=self.cheat_flag, onvalue=1, offvalue=0).pack(side=TOP, anchor='w')
        Checkbutton(frame1, text='最小化运行', variable=self.min_flag, onvalue=1, offvalue=0).pack(side=TOP, anchor='w')
        Button(frame1, command=lambda: stop(), text='停止', width=20).pack(side=TOP, expand=YES)

        self.app.protocol("WM_DELETE_WINDOW", '')
        Window.LogUI = t3
        t3.insert(END, '>>>-注意目标图片及路径请勿带中文-<<<\n')
        self.app.bind("<Key>", short_cut)
        self.app.mainloop()  # 窗口的主事件循环，必须的。


if __name__ == '__main__':
    app = Window()
