#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c']


# 列表合并
"""'+'进行合并，相当于字符串合并"""
list_3 = list_1 + list_2  # 返回新列表
print(list_3)
print(list_1)
list_1 += list_2    # 合并后存放到list_1
print(list_1)
print(list_2)


# enumerate() ——枚举函数，获取列表的元素下标和元素
num = [1, 20, 30, ]
for i in enumerate(num):
    print(i)
