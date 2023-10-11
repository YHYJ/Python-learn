#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""读取 ./Data/pi_digits.txt 整个文件并打印到屏幕"""


file_path = './Data/pi_digits.txt'     #文件路径

with open(file_path) as file:
    contents = file.read()
    print(type(contents))
    print(contents.strip())
'''
如果文件不存在，open()函数抛出一个IOError
open()函数返回一个表示文件的对象存储到变量file，此时已打开文件

read()方法读取文件全部内容赋到contents变量，文件内容用一个str对象表示

文件末尾有一个\n，显示出来是一个空行，可以使用strip()删除多出来的空行
'''