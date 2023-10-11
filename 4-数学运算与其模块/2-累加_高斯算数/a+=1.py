#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 任意给定一个最高值num，,求1+2+3+……+num的值
print('给定一个值，计算从1累加到这个值的得数')


max_Num = int(input('请输入任意整数：'))
de = 0
for i in range(1, max_Num+1):
    de += i
print(de)
