#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-03 22:03:03
Last modified: 2018-01-03 22:03:03
Author: YJ1516 - yj1516268@outlook.com

"""


def mylist(alist):
    """
    扩展一个列表，列表元素可能还是一个列表
    """
    newlist = []
    for i in alist:
        if isinstance(i, list):
            newlist.extend(mylist(i))
        else:
            newlist.append(i)
    return newlist


alist = [1, 2, 5, [3, [], 5, 2, [57]], 90]
print(mylist(alist))
