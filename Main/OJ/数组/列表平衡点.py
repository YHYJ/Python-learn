#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-04 14:04:01
Last modified: 2018-01-04 14:04:01
Author: YJ1516 - yj1516268@outlook.com

找出一个列表的平衡点（即该平衡点左右两边元素和相等）
"""


def fore(list_):
    sumT = sum(list_)
    balance = 0
    for num in list_:
        if balance < (sumT-num)/2:
            balance += num
        else:
            break
    if balance == (sumT-num)/2:
        print("平衡点是：{0}".format(num))
    else:
        print("没有平衡点")


if __name__ == '__main__':
    numbers = [1, 3, 2, 4, 15, 26, 4, 11, 10]
    fore(numbers)
