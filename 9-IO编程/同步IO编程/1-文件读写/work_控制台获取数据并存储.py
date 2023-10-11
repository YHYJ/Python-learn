#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 从控制台获取内容，写入到work2.txt保存
data1 = input('请输入你要写入的内容：')

with open('./Data/work2第一.txt','a') as wr:
    wr.write(data1 + '\n')