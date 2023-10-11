#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-04 15:57:59
Last modified: 2018-01-04 15:57:59
Author: YJ1516 - yj1516268@outlook.com

"""

alist = [1, 2, 1, 3, 4, 2]


def func(alist):
    """
    迭代列表，判断元素是否在一个空列表中，否则添加到该列表
    :return result 不重复元素组成的新列表
    """
    result = []
    for i in alist:
        if i not in result:
            result.append(i)
    return result


fun = func(alist)
print(fun)
