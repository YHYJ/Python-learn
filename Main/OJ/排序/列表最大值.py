#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-03 19:36:17
Last modified: 2018-01-03 19:36:17
Author: YJ1516 - yj1516268@outlook.com

"""

alist = [4, 26, 22, 17, 46, 31, 44, 3, 23]


x = alist[0]
for y in alist[1:]:
    if x < y:
        x = y
print(x)
