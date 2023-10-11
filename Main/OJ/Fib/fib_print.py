#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-03 21:35:57
Last modified: 2018-01-03 21:35:57
Author: YJ1516 - yj1516268@outlook.com

"""


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1


fib(10)
