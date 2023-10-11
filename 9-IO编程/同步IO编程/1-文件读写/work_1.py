#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""访客：
提示用户输入其名字，用户输入完成将其名字写入到文件 guest.txt 中
"""

file_name = './Data/guest.txt'
name = input("请输入用户名:")
with open(file=file_name,mode='a') as file_object:
    file_object.write(name + '\n')