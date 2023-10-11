#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

while 1:
    try:
        t = int(input('请输入:'))
        p = int(input('请输入:'))
    except EOFError:
        break
    print('相加得：', t + p)
    print('相减得：', t - p)
    print('相乘得：', t * p)
    print('相除得：', t / p)