import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from mouse_helper.thread_initiator import ThreadInitiator
# 导入消息对话框子模块
import tkinter.filedialog

tasks = []


# 新建脚本
def create_script():
    # 选择保存文件路径
    path = tkinter.filedialog.asksaveasfilename()
    print(path)


# 运行脚本
def run_script():
    # 获取文件路径
    path = tkinter.filedialog.askopenfilename()
    print(path)


def start(target, log):
    # 创建新线程
    threadInitiator = ThreadInitiator(target, log=log)
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
        Button(frame1, command=create_script, text='创建脚本', width=20).pack(
            side=TOP, expand=YES)
        Button(frame1, command=run_script, text='运行脚本', width=20).pack(
            side=TOP, expand=YES)
        Checkbutton(frame1, text='循环执行', command=loop).pack(side=TOP, anchor='w')
        Checkbutton(frame1, text='随机偏移', command=cheat).pack(side=TOP, anchor='w')
        Button(frame1, command=lambda: stop(), text='停止', width=20).pack(side=TOP, expand=YES)

        self.app.protocol("WM_DELETE_WINDOW", '')
        Window.LogUI = t3
        self.app.bind("<Key>", short_cut)
        self.app.mainloop()  # 窗口的主事件循环，必须的。


if __name__ == '__main__':
    app = Window()
