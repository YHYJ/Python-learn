#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-17 15:46:22
Last modified: 2017-09-17 15:46:22
Python release: 3.6.2

互相调用死锁
两个函数中调用相同的资源，互相等待对方结束
两个线程分别占有一部分资源并且同时等待对方的资源，造成互相调用死锁
"""


import threading
import time

resA = 0
resB = 0

class MyThread(threading.Thread):
    def do1(self):
        global resA, reaB
        if mutexA.acquire():
            msg = self.name + ' got resA '
            print(msg)
            if mutexB.acquire():
                msg = self.name + ' got resB '
                print(msg)
                mutexB.release()
            mutexA.release()
    def do2(self):
        global resA, resB
        if mutexB.acquire():
            msg = self.name + ' 2_got resB '
            print(msg)
            if mutexA.acquire():
                msg = self.name + ' 2_got resA '
                print(msg)
                mutexA.release()
            mutexB.release()
    def run(self):
        self.do1()
        self.do2()

mutexA = threading.Lock()
mutexB = threading.Lock()

def test():
    for _ in range(3):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    test()

