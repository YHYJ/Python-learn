#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-03 19:36:17
Last modified: 2018-01-03 19:36:17
Author: YJ1516 - yj1516268@outlook.com

"""

alist = [4, 26, 22, 17, 46, 31, 44, 3, 23]


def mp(alist):
    """快速排序，递归
    将列表的值与列表的第0个元素比较
    小于的放到列表smalllist，大于的放到列表biglist
    将这两个列表作为参数递归调用该函数进行比较
    最后加上位于两个列表中间的原始列表的第0个元素
    """
    if alist == []:
        return alist
    smalllist = []
    biglist = []
    middle = alist[0]
    for i in alist[1:]:
        if i < middle:
            smalllist.append(i)
        else:
            biglist.append(i)
    return mp(biglist) + [middle] + mp(smalllist)


mp_f = mp(alist)
print(mp_f)
