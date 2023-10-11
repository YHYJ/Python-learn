#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
append() ——在列表末尾添加元素
insert() ——在列表任意位置插入元素
extend([list]) ——向list中添加另一个列表的所有元素
"""


# append() ——在列表末尾添加元素
print('*'*25, '在列表末尾添加元素', '*'*25)
'''这种创建列表的方式极其常见
因为经常要等程序运行后才知道用户要在程序中存储哪些数据.
为控制用户，可首先创建一个空列表，用于存储用户将要输入的值-
-然后将用户提供的每个新值附加到列表中
'''
lista = ['honda', 'yamaha', 'suzuki']
lista.append('ducati')
print(lista)
'''append()动态创建列表，可以先创建一个空列表，再添加元素'''


# insert() ——在列表任意位置插入元素
print('*'*25, '在列表末尾添加元素', '*'*25)
listb = ['honda', 'yamaha', 'suzuki']
listb.insert(1, 'ducati')
print(listb)
'''可在任何位置添加元素，只需要新元素的索引和值'''


# extend([list]) ——向list中添加另一个列表的所有元素
print('*'*25, '向list中添加另一个列表的所有元素', '*'*25)
'''通过添加一个列表中所有的元素来扩展原有列表，等同于 a[len(a):] = L'''
listc = ['honda', 'yamaha', 'suzuki']
listc.extend(['1', '2'])
print(listc)