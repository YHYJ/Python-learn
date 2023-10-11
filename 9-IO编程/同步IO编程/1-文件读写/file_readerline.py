#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""按行读取 ./Data/pi_digits.txt 文件并打印到屏幕."""

file_path = './Data/pi_digits.txt'

with open(file=file_path) as file:
    print(file)             # 文件信息
    for line in file:       # 逐行读取
        print(line.strip())


print("*"*100)

"""在with中创建一个包含文件各行内容的列表，在with外调用"""
with open(file=file_path) as file_object:
    lines = file_object.readlines()     #readlines()方法读取每一行，readline()方法只读取第一行

print(lines)    #已按行存储到列表lines中
for line in lines:
    print(line.strip())