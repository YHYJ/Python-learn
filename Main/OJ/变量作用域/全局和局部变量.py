#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-06 19:44:03
Last modified: 2018-01-06 19:44:03
Author: YJ1516 - yj1516268@outlook.com

num是局部变量，每个函数获得的都是它的拷贝，修改不共享，除非用 global 声明
"""


num = 9


def f1():
    global num
    num = 20
    print(num)


def f2():
    print(num)


f2()    # 9
f1()    # 20
f2()    # 9
