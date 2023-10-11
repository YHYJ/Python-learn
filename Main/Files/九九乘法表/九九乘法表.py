#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""打印标准格式九九乘法表"""


x = 1
while x <= 9:   # 先确定行数
    y = 1
    while y <= x:   # 再确定每行的元素个数
        print('%dx%d=%d' % (y, x, x*y), end='  ')
        y += 1
    print()
    x += 1
