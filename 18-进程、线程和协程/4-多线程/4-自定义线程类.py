#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""当一类函数功能相似而需要各自运行，就自定义线程类"""


import threading


class MyThread(threading.Thread):
    """自定义线程类"""

    def __init__(self, name='YJ'):
        # 用到父类的参数的话就调用父类构造函数
        super(MyThread, self).__init__()
        self.name = name

    def show(self):
        """自定义线程要执行的任务"""
        for _ in range(6):
            print(self.name)

    def run(self):
        """mythread.start()会调用run()方法里的方法"""
        self.show()


if __name__ == '__main__':
    mythread = MyThread(name='YJ1516')
    mythread.start()
