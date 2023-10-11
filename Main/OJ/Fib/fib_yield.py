#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-03 21:39:53
Last modified: 2018-01-03 21:39:53
Author: YJ1516 - yj1516268@outlook.com

"""


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


for i in fib(10):
    print(i)
