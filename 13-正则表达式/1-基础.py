#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""正则表达式用来匹配字符串
它用一种描述性的语言来给字符串定义一个规则,符合规则的字符串就认为它“匹配”了
否则，该字符串就是不合法的"""


import re


text = "His, I am Shirley hislton. I am wife."

# r 的意思
'''r = raw，表示对字符串不进行转义而保持原样，因为py的字符串碰到 "\" 就会转义它后面的字符'''
print("\bhi")   # [hi]
print("\\bhi")  # [\bhi]    \\b，转义为输出\
print(r"\bhi")  # [\bhi]    r"\b"，不进行转义输出\bhi
print(r"\\bhi")  # [\\bhi]   r"\\bhi"，不进行转义输出\\bhi


# 1:最简单的正则表达式，完全/精确匹配
m = re.findall(r"hi", text)
if m:
    print(m)
else:
    print("nothing")

# 2:找到独立的"Hi",忽略包含Hi的单词，用 \b……\b
m = re.findall(r"\b[Hh]is\b", text)  # \b 代表它所占据的位置是空格、标点、换行……
if m:
    print(m)
else:
    print("nothing")

# 单独匹配多个字符中的一个，用[]
m = re.findall(r"[Hh]i", text)
if m:
    print(m)
else:
    print("nothing")
