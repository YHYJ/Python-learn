#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""利用Py的特性过滤文件"""


import os

"""列出当前目录下的所有目录"""
# 只需要一行代码：
#print([x for x in os.listdir('.') if os.path.isdir(x)])

"""列出所有的.py文件"""
# 只需一行代码：
#print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


"""work"""
# 1、利用os模块编写一个能实现dir -l输出的程序
# 2、在当前目录及其所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
def search(path, text):
    for file in os.listdir(path):                                # 1
        if os.path.isfile(os.path.join(path, file)):              # 2
            if text in os.path.splitext(file)[0] or text in os.path.splitext(file)[1]:                # ３
                print('相对路径： %s\n文 件 名： %s\n' % (path, file))  # 4
        if os.path.isdir(os.path.join(path, file)):               # 5
            search(os.path.join(path, file), text)                # 6

search(path='.',text='s')
'''
1：listdir(path) —— 返回path下文件(夹)名的列表。然后遍历
2：join(path,file) —— 将路径名(path)和其下的文件(夹)名(file)连接起来；isfile() —— 测试path+file是否是文件名而不是目录名
3：是普通文件的话分割(splitext(file))文件名并测试text指定的str是否在文件名中
4：text在文件名中的话打印文件的相对路径和文件名
5：isdir() —— 测试path+file是否是目录名而不是文件名
6：是目录名的话将目录名当做path参数再次传入search()函数以查询这个次级目录下是否有包含text参数指定str的文件
'''