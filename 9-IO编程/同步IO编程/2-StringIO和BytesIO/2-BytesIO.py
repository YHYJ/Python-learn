#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO"""


"""BytesIO实现了在内存中读写bytes"""
# 创建一个BytesIO，然后写入一些bytes：
from io import BytesIO
file = BytesIO()
file.write('中文'.encode('utf-8'))        # 长度为6
file.write('English'.encode('utf-8'))     # 长度为7
print(file.getvalue())      # 写入的不是str，而是经过UTF-8编码的bytes

"""读取BytesIO"""
# 用一个bytes初始化BytesIO，然后像读文件一样读取：
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
fs = f.read()
print(fs.strip())

"""小结：
StringIO和BytesIO是在内存中操作str和bytes的方法
和读写文件具有一致的接口
"""