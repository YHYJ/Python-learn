#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-04 15:57:59
Last modified: 2018-01-04 15:57:59
Author: YJ1516 - yj1516268@outlook.com

保持列表中元素的顺序，对列表去重，复杂度为O(n)
"""

alist = [1, 2, 1, 3, 4, 2]


def fund(alist):
    result = []
    temp = set()
    for i in alist:
        if i not in temp:
            result.append(i)
            temp.add(i)
    return result


fun = fund(alist)
print(fun)
