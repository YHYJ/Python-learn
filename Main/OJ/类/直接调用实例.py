#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-06 18:43:51
Last modified: 2018-01-06 18:43:51
Author: YJ1516 - yj1516268@outlook.com

"""


class A(object):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print('a=', self.__a, 'b=', self.__b)

    def __call__(self, num):
        print("call:", num + self.__a)


a1 = A(15, 20)
a1.myprint()
a1(80)  # 为使类的实例对象能被直接调用，需要实现类的__call__方法
