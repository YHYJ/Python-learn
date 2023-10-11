#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-06 18:53:41
Last modified: 2018-01-06 18:53:41
Author: YJ1516 - yj1516268@outlook.com

输出是什么
"""


class B(object):
    def fn(self):
        print('B fn')

    def __init__(self):
        print("B INIT")


class A(object):
    def fn(self):
        print('A fn')

    def __new__(cls, a):
        print("NEW", a)
        if a > 10:
            return super(A, cls).__new__(cls)
        return B()

    def __init__(self, a):
        print("INIT", a)


a1 = A(5)
a1.fn()
a2 = A(20)
a2.fn()
"""
NEW 5       # 调用A的__new__方法
B INIT      # 因为5，所以返回B()
B fn        # 因此a1是B的实例对象，执行B的fn()方法
NEW 20      # 调用A的__new__方法
INIT 20     # 因为20，所以new了一个A的对象
A fn        # 因此a2是A的实例对象，执行A的fn()方法
"""
