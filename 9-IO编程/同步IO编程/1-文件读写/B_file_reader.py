#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""读取二进制文件 —— 一张照片"""


file_path = './Data/06.jpg'     #文件路径

with open(file_path,mode='rb',errors='ignore') as f:
    file = f.read()
    print(file)     # 输出十六进制表示的字节