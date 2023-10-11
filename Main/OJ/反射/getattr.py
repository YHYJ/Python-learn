#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-06 15:42:17
Last modified: 2018-01-06 15:42:17
Author: YJ1516 - yj1516268@outlook.com

Python的反射机制：
接受一个对象或者模块，在里面查找一个叫str的成员
查找：getattr(name, str)
判断：hasattr(name, str)
删除：delattr(name, str)
添加：setattr(name, str)
创建一个类，输出一个属性，有则输出它的值，否则输出属性名
"""


class MyGetattr:
    def __init__(self):
        self.A = 1.0

    a = 0.1

    def __getattr__(self, name):
        return name


cc = MyGetattr()
print(cc.a, cc.b, cc.A)

print(getattr(cc, 'a'))
print(getattr(cc, 'b'))
