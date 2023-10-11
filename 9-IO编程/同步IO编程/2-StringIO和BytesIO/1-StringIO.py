#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""数据读写不一定是操作文件，也可以在内存中读写"""


"""StringIO就是在内存中读写str
要把str写入内存，需要先创建一个StringIO"""
# 然后像文件一样写入即可：

from io import StringIO

file = StringIO()
file.write('Hello')     # 以print打印会输出字符串长度
file.write(' ')
file.write('world!')
print(file.getvalue())  # getvalue()方法用于获得写入后的str


"""读取StringIO"""
# 用一个str初始化StringIO，然后像读文件一样读取：
f = StringIO('Hello!\nHi!\nGoodbye!\n')     # 初始化StringIO
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
