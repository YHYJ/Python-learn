#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""打印菱形"""

for i in range(1, 9+1, 2):  # 正三角形
    print((i * '*').center(9))      # 决定每行多少点数和每行长度

for i in range(9-2, 0, -2):  # 倒三角形
    print((i * '*').center(9))


def printf(hang):
    for i in range(1, hang+1, 2):       # 正三角形
        print((i*'*').center(hang))

    for i in range(hang-2, 0, -2):       # 倒三角形
        print((i*'*').center(hang))

if __name__ == '__main__':
    hang = int(input('请输入菱形最宽处点数(正奇数)：'))
    printf(hang)