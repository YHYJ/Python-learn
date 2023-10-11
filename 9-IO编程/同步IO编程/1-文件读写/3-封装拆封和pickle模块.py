#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""pickle模块
pickle模块将一个Py对象按照一定的规范序列化为一段字节流
以便将它保存到一个文件、存储到数据库或者通过网络传输
下次使用时，从文件中读出文本，再按照此规范解析这些数据
这种将对象状态转换为可保存或传输的文本的过程叫做‘封装’或者‘序列化’
对应的，从封装的格式中解析对象状态的过程被称为‘拆封’或者‘反序列化’"""

import pickle as pi    # 模块重命名为pi


data = ['Save me',123.456,True,False,0,1]
file_path = './Data/pickle.data'

"""封装：有一个数据对象data，和一个有写权限的文件对象file"""
# 可用dump()，最简单的封装仅一行代码：
with open(file_path,'wb') as file:
    pi.dump(data,file)


"""拆封：对已封装的文件对象myfile进行拆封"""
# 可用load()或loads()重构这个对象：
with open(file_path,'rb') as myfile:
    txt = pi.load(myfile)
    print(txt)