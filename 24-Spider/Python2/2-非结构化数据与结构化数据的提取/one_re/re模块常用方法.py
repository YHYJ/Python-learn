#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""内置正则模块re"""

import re


"""使用步骤：
1. 使用 compile() 函数将正则表达式编译为一个 Pattern 对象
2. 通过 Pattern 对象提供的一系列方法对文本进行匹配查找，获得一个 Match 对象作为匹配结果
3. 使用 Match 对象提供的属性和方法获得信息，根据需要进行其他操作
"""


# compie()函数
"""用于编译正则表达式，生成一个 Pattern 对象"""
pattern = re.compile(r"\d+")


# Pattern对象的常用方法
"""match方法"""
'''用于查找字符串头部（可以指定起始位置）；一次性匹配，只能匹配到一个正确结果；'''
match = pattern.match("one12twothree34four", pos=3)  # post=3指定匹配区间
print(match)    # 返回一个 Match 对象（分组）
print(match.group(0))   # 返回全部匹配
print(match.start(0))   # 返回匹配结果的起始索引
print(match.end(0))     # 返回匹配结果的结束索引+1
print(match.span(0))    # 返回匹配结果的(开始, 结束)索引

"""search方法"""
'''用于查找字符串任意位置；一次性匹配；'''
search = pattern.search("one12twothree34four", pos=10, endpos=30)
print(search)
if search:
    print("匹配结果：{}".format(search.group()))
    print("结果索引：{}".format(search.span()))

"""findall方法"""
'''完全匹配；返回一个元素为字符串的列表；'''
findall = pattern.findall("one12twothree34four")
print(findall)  # 匹配结果是元素为字符串的列表
for i in findall:
    print(i)

"""finditer方法"""
'''类似findall；完全匹配；返回一个迭代器；'''
finditer = pattern.finditer("one12twothree34four", 0, 10)
print(finditer)   # 迭代器
print(type(finditer))
for i in finditer:
    print("匹配结果：{}，结果索引：{}".format(i.group(), i.span()))

"""split方法"""
'''按照切割规则将字符串分割后返回列表；'''
pattern_split = re.compile(r"[\s\,\;]+")    # 切割规则
split = pattern_split.split("a,b;; c   d", maxsplit=2)  # 指定最大分割次数
print(split)

"""sub方法"""
'''替换；'''
'''使用形式：
sub(repl, string[, count])
其中，repl 可以是字符串也可以是一个函数：
    1. 如果 repl 是字符串，则会使用 repl 去替换字符串每一个匹配的子串，
       并返回替换后的字符串，另外，repl 还可以使用 id 的形式来引用分组，
       但不能使用编号 0
    2. 如果 repl 是函数，这个方法应当只接受一个参数（Match 对象），
       并返回一个字符串用于替换（返回的字符串中不能再引用分组）
count 用于指定最多替换次数，不指定时全部替换
'''
# repl是字符串
pattern_sub = re.compile(r"(\w+) (\w+)")
mate_str = "hello 123, hello 456"
print(pattern_sub.sub(r"hello world", mate_str))   # 使用 'hello world' 替换 mate_str
print(pattern_sub.sub(r"\2 \1", mate_str))  # 将pattern_sub指定的分组1、2调换


def func(mate_str):
    # repl是函数
    return "hi" + " " + mate_str.group(1)


print(pattern_sub.sub(func, mate_str))      # mate_str是函数func()的参数
print(pattern_sub.sub(func, mate_str, 1))
