#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-06 20:38:17
Last modified: 2018-01-06 20:38:17
Author: YJ1516 - yj1516268@outlook.com

写一个函数，接收整数参数num，返回一个函数，功能是把它的参数和num相乘并把结果返回
"""


def closure(num):
    def func(n):
        return n * num
    return func


clo = closure(12)
print(clo(6))
