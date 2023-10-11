#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-03 21:50:19
Last modified: 2018-01-03 21:50:19
Author: YJ1516 - yj1516268@outlook.com

可变类型作为参数
当显式传递参数时（比如test(1, [3, 2, 1])），每次函数调用不会互相影响
当不传递参数时，每次函数调用时该可变参数都是共用的，
即上次不传参调用对可变参数的修改会延续到下一次不传参调用的最终结果
"""


def test(x, l=[0]):
    for o in range(x):
        l.append(o)
    print(l)


test(3)
test(1, [3, 2, 1])
test(5)
