#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-06 15:06:14
Last modified: 2018-01-06 15:06:14
Author: YJ1516 - yj1516268@outlook.com

考察闭包
lambda函数共用i变量
"""


x = [lambda x: x*i for i in range(3)]   # x是一个匿名函数列表
y = [o(2) for o in x]
print(y)    # [4, 4, 4]


def func():
    """正确写法"""
    def funx(x):
        def funy(y):
            return x*y
        return funy
    return [funx(one) for one in range(3)]


fun = func()
li = [o(2) for o in fun]
print(li)   # [0, 2, 4]
