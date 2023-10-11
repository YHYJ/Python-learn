#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""格式化字符串，使其对齐或者改变大小写"""


string = 'hello woRld Str'

# 对齐
print('*'*25, "对齐", '*'*25)
'''第一个参数参数指需要对齐的字符串加上空格总共占的宽度
可以给定第二个参数指出用什么字符填充，用来填充的字符串本身长度必须为1
操作结果是一份原字符串的拷贝，原字符串不变'''
# ljust() ——左对齐
print('|', string.ljust(10), '|')
# rjust() ——右对齐
print('|', string.rjust(10), '|')
# center() ——居中
print('|', string.center(10), '|')
'''第二个参数指定用来填充的字符串，其本身长度必须为1'''
print('|', string.center(10, '*'), '|')


# 改变大小写
print('*'*25, "改变大小写", '*'*25)
'''只允许其指定的字符成为其指定的格式，比如string里的R和S'''
# captalize() ——不管里面有几个单词，只大写第一个字符
print(string.capitalize())
# title() ——改变字符串其中每个单词首字母的大小写
print(string.title())
# upper()和lower() ——全部改为大写或小写
print(string.upper())   # 全部字符为大写
print(string.lower())   # 全部字符为小写
'''存储数据时lower()很有用
很多时候用户不会提供正确的大小写，因此可以先将字符串全转换为小写再存储'''
# 大小写互换 ——大写转小写，小写转大写
print(string.swapcase())
