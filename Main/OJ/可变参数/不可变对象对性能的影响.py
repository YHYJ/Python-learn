#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-06 20:42:40
Last modified: 2018-01-06 20:42:40
Author: YJ1516 - yj1516268@outlook.com

下面代码慢在哪
str1是个不可变对象，每次迭代都要生成新的str1对象来存储新的字符串，num越大，内存开销越大
"""


def strtest1(num):
    str1 = 'first'
    for i in range(num):
        str1 += "X"
        return str1


strt = strtest1(12)
print(strt)
