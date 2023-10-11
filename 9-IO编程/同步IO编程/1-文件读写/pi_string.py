#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用文件中的内容."""


print("*"*25 + "创建一个字符串，包含文件中存储的所有数字，且没有任何空格" + "*"*25)
#
file_path = './Data/pi_digits.txt'

with open(file_path) as file:
    lines = file.readlines()    # 按行存储到列表 lines 中

pi_string = ''      # 创建字符串 pi_string 来存储 pi_digits.txt 的内容
for line in lines:
    pi_string += line.strip()   # 将两边的空格都消除

print(pi_string[:30] + "...")   # 打印前30个
print(len(pi_string))
'''读取文本文件时， Py将其中的所有文本都解读为字符串
如果读取的是数字，并要将其作为数值使用
必须使用函数int()或float()将其转换为数值型
'''


print("*"*25 + "检查文件中是否包含某个字符串" + "*"*25)
#
with open(file_path) as file_objrcts:
    lines = file_objrcts.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("输入你的生日（只包含数字）：")
if birthday in pi_string:
    print("你的生日包含在π的前%d位" % len(pi_string))
else:
    print("你的生日没有包含在π的前%d位" % len(pi_string))