#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-17 15:15:41
Last modified: 2017-09-17 15:15:41
Python release: 3.6.2

迭代死锁
"""


import threading
import time

class Mythread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        
        if mutex.acquire(1):
            num += 1
            msg = self.name + ' set num to ' + str(num)
            print(msg)
            # mutex.acquire()   # 注释第一个acquire...release中的第二次acquire
            # mutex.release()   # 取消死锁
            mutex.release()
num = 0
mutex = threading.Lock()
def test():
    for _ in range(5):
        t = Mythread()
        t.start()

if __name__ == '__main__':
    test()
'''run()函数的第一行if语句第一次请求资源，请求后未relase释放资源，再次acquire
最终无法释放，通过注释第一次acquire中的第二次acquire取消死锁状态，
也可以通过可重入锁解决'''

