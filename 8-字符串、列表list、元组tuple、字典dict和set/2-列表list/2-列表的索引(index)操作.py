#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
用[]加序号访问list的方式就是索引(index)操作
遍历list的元素
访问list中的元素
替换list中的元素
"""


I = [365, 'everyday', 0.618, True]
print(I.index(0.618))   # 查找0.618的下标

# 遍历list的元素
print('*'*25, '遍历list的元素', '*'*25)
for i in I:
    print(i)


# 访问list中的元素
print('*'*25, '访问list中的元素', '*'*25)
print(I[0])  # 访问第0个元素
print(I[1])  # 访问第1个元素
'''除了正数索引外，list还可以处理负数的索引'''
print(I)
print(I[-1])    # list I中的最后一个元素
print(I[-3])    # list I中的倒数第三个元素


# 替换list中的元素
print('*'*25, '替换list中的元素', '*'*25)
I[3] = 998
print(I)
