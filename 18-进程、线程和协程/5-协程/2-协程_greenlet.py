#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-24 15:35:39
Last modified: 2017-09-24 15:35:39
Python release: 3.6.2

greenlet模块对协程进行了封装，缺点是还需要人工切换
"""


import time
from greenlet import greenlet

def test1():
    while True:
        print("---test1---")
        gl2.switch()
        print("测试1...")
        time.sleep(0.5)


def test2():
    while True:
        print("---test2---")
        gl1.switch()
        print("测试2...")
        time.sleep(2.5)


if __name__ == "__main__":
    gl1 = greenlet(test1)
    gl2 = greenlet(test2)

    # 切换到gl1中运行
    gl1.switch()

