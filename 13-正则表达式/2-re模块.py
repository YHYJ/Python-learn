#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Py提供re模块，包含所有正则表达式的功能"""

import re


# re.findall(r"hi",text)
'''re是python里的正则表达式模块。
findall是其中一个方法，用来按照提供的正则表达式，去匹配文本中的所有符合条件的字符串。
返回结果是一个包含所有匹配结果的list'''


# 由于Py的字符串本身也用\转义，所以强烈建议使用r前缀，就不用考虑转义的问题了：
s = 'ABC\\-001'     # Py的字符串
# 要匹配s，对应的正则表达式字符串变成：'ABC\-001'
s_1 = r'ABC\-001'   # Py的字符串
# 匹配s_1，对应的正则表达式字符串不变：'ABC\-001'


# 判断正则表达式是否匹配：
'''match()方法判断是否匹配，匹配成功返回一个Match对象，否则返回None'''
print(re.match(r'^\d{3}\-\d{3,8}$', '101-123456'))

# 常见的判断方法：
string = input('用户输入的字符串：')
if re.match(r'正则表达式', string):
    print('yes')
else:
    print('no')
