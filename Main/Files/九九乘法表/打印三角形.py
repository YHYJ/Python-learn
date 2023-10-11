#!/usr/bin/env python3
# -*- coding: utf-8 -*-


for i in range(1, 12):              # 行数(12-1)
    if i <= 6:                      # 第6行为顶点
        for j in range(1, i+1):     # 每行的点数，正立三角形最长为6
            print('*', end=' ')     # 打印1~6行
    else:
        for j in range(1, 12-i+1):  # 倒立三角形最长为5
            print('*', end=' ')
    print()


def printf(long):
    for i in range(1, long*2):
        if i <= int(long):
            for j in range(1, i+1):
                print('*', end=' ')
        else:
            for j in range(1, long*2-i+1):
                print('*', end=' ')
        print()

if __name__ == '__main__':
    long = int(input('请输入三角形边长(正整数)：'))
    printf(long)
