#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-06 18:36:36
Last modified: 2018-01-06 18:36:36
Author: YJ1516 - yj1516268@outlook.com

通过类B的对象，调用类A的方法
"""


class A(object):
    def show(self):
        print("Super Class A")


class B(A):
    def show(self):
        print("Super Class B")


class C(object):
    def show(self):
        print("Super Class C")


obj = B()
obj.show()

obj.__class__ = A       # __class__方法指向类对象，赋值为A即可
print(obj.__class__)
obj.show()
obj.__class__ = C
print(obj.__class__)
obj.show()
