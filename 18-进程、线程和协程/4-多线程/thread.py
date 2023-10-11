#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-13 19:51:44
Last modified: 2017-09-13 19:51:44
Python release: 3.6.2

最简单的多线程
"""


import threading
import time

def sayhi():
    print("Hi, i'm your future")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=sayhi, name='SayHi')
        print("线程 %s_%d 正在运行..." % (threading.current_thread().name, i))
        t.start()
