#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
tell() ——定位文件指针当前位置
seek(offset, from) ——将文件指针定位到指定位置
    offset：偏移量
    from：方向，0表示文件开头，1表示当前位置，2表示文件末尾
"""


with open('./Data/1516.txt') as f:
    # 定位文件指针当前位置
    file = f.read(3)
    print('该文件编码：', f.encoding)
    print('前3字节数据是：', file)
    print('当前文件指针位置：', f.tell())
    file = f.read(2)
    print('4,5字节数据是：', file)
    print('当前文件指针位置：', f.tell())
    # 将文件指针定位到指定位置
    f.seek(15, 0)
    print(f.read(3))
