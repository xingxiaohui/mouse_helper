"""
线程支持类，用于启动线程调用脚本方法
"""
import threading
import time
from tkinter import END

from mouse_helper import main

titles = {'create_script': '录制脚本', 'run_script': '执行脚本', 'image_click': '截图点击'}


class ThreadInitiator(threading.Thread):
    def __init__(self, app, target, file_path, log, loop_flag, cheat_flag, min_flag):
        threading.Thread.__init__(self)
        self.flag = True
        self.target = target
        self.file_path = file_path
        self.loop_flag = loop_flag
        self.cheat_flag = cheat_flag
        self.min_flag = min_flag
        self.log = log
        self.app = app

    def run(self):
        self.log.insert(END, time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime(time.time())) + '开始' + titles[str(self.target)] + '\n')
        if self.target == 'create_script':
            self.log.insert(END, '倒计时5秒后开始执行鼠标点击\n')
            time.sleep(5)
            if self.min_flag == 1:
                self.app.iconify()  # 最小化窗口
            main.create_script(self.app, self.file_path, log=self.log)

        if self.target == 'run_script':
            self.log.insert(END, '倒计时5秒后开始执行鼠标点击\n')
            time.sleep(5)
            if self.min_flag == 1:
                self.app.iconify()  # 最小化窗口
            while self.flag:
                main.run_script(self.app, self.file_path, self.cheat_flag, log=self.log)
                # 退出循环
                print('self.loop_flag')
                print(self.loop_flag)
                if self.loop_flag == 0:
                    self.flag = False

        if self.target == 'image_click':
            image_list = main.get_image_path_list(self.file_path)
            self.log.insert(END, '倒计时5秒后开始执行鼠标点击\n')
            self.log.see(END)
            time.sleep(5)
            if self.min_flag == 1:
                self.app.iconify()  # 最小化窗口
            while self.flag:
                main.image_click(self.app, self.cheat_flag, image_list, log=self.log)
                # 退出循环
                if self.loop_flag == 0:
                    self.flag = False

        self.log.insert(END, time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime(time.time())) + '结束操作\n')
        self.log.see(END)

    def stop(self):
        self.flag = False
