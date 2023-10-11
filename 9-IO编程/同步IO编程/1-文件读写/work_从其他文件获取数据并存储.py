#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 从1516.txt中读取内容，写入到work1.txt保存

with open('./Data/1516.txt') as re:  # 打开1516.txt
    data = re.read()                 # 读取至data

with open('./Data/work1.txt','a') as wr:    # 写入work1.txt
    wr.write(data + '\n')