#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
in/not in
index() ——查找元素
count() ——计算元素在列表中出现的次数
"""


li = [365, 'everyday', 0.618, True, 365]

# index() ——查找元素
print('*'*25, '查找元素', '*'*25)
'''返回列表中指定元素的索引，如果没有该元素就会报错'''
print(li.index(0.618))


# count() ——计算元素在列表中出现的次数
print('*'*25, '元素计数', '*'*25)
'''计算元素365在列表中出现的次数'''
print(li.count(365))
print(li.count(1))  # 计数时元素 True 看做 1 ， False 看作 0
