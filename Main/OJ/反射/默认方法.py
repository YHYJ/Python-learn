#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-06 20:01:47
Last modified: 2018-01-06 20:01:47
Author: YJ1516 - yj1516268@outlook.com

修改代码，使调用未定义方法时默认调用mydefault()方法
"""


class A(object):
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
        print('init')

    def mydefault(self, args):
        print('default：{}'.format(args))

    def __getattr__(self, name):
        return self.mydefault


a1 = A(10, 20)
a1.fn1(1)
a1.fn2("2")
a1.fn3('3')
