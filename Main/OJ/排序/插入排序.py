#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-03 19:36:17
Last modified: 2018-01-03 19:36:17
Author: YJ1516 - yj1516268@outlook.com

"""

alist = [4, 26, 22, 17, 46, 31, 44, 3, 23]


def insert_sort(alist):
    """插入排序
    0 1 2 3 4 5 6 7
    1 2 3 4 5 6 7 8
    """
    for i in range(len(alist) - 1):
        for j in range(i + 1, len(alist)):
            if alist[i] < alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist


ins = insert_sort(alist)
print(ins)
