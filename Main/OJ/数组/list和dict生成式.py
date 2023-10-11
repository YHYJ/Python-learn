#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-06 19:36:00
Last modified: 2018-01-06 19:36:00
Author: YJ1516 - yj1516268@outlook.com

列表生成式和字典生成式
"""


ls = [1, 2, 3, 4]

list1 = [i for i in ls if i > 2]
print(list1)    # [3, 4]

list2 = [i*2 for i in ls if i > 2]
print(list2)    # [6, 8]

dic1 = {x: x**2 for x in (2, 4, 6)}
print(dic1)     # {2: 4, 4: 16, 6: 36}

dic2 = {x: 'item' + str(x**2) for x in (2, 4, 6)}
print(dic2)     # {2: 'item4', 4: 'item16', 6: 'item36'}

set1 = {x for x in 'hello world' if x not in 'low level'}
print(set1)     # {'h', 'r', 'd'}
