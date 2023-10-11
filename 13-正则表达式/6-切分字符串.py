#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""正则表达式切分字符串比用固定的字符更灵活"""

import re

# 正常的切分代码：
print('a b  c 1 1'.split(' '))
'''输出：['a', 'b', '', 'c', '1', '1']，无法识别连续的空格'''

# 正则表达式切分代码：
print(re.split(r'\s+', 'a,c,  d, f'))
print(re.split(r'[\s\,\;]+', 'a,c,;;  d, f'))

'''如果用户输入了一组标签，用正则表达式来把不规范的输入转化成正确的数组'''
