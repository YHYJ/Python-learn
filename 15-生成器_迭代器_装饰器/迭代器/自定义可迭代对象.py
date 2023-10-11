#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-21 15:31:36
Last modified: 2017-09-21 15:31:36
Python release: 3.6.2

一个具备了__iter__方法的对象，就是一个可迭代对象
"""


from collections import Iterable


class MyList(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    def __iter__(self):
        """返回一个迭代器"""
        pass

mylist = MyList()
print(isinstance(mylist, Iterable))

"""添加__iter__方法，mylist对象已经是一个可迭代对象"""
