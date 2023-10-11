#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#对于单个字符的编码，Python提供了 ord() 函数获取字符的整数表示， chr() 函数把编码转换为对应的字符
a = ord('A')
b = ord('嘻')
c = chr(65)
d = chr(22985)
print('a =',a,'\nb =',b,'\nc =',c,'\nd =',d)


"""
Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干字节，
如果要在网络上传输或者存储起来，就要把str转为bytes
"""
#Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
'''
注意区分 'ABC' 和 b'ABC' ，
前者是str，后者虽然内容显示得和前者一样，
但bytes的每个字符都只占用一个字节
'''

print("""""")

#计算str或者bytes包含多少字符，用 len() :
print(len('AbC'))
print(len('中文CN'))
print(len(b'AbC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

print("""""")

# 1.str转bytes——以Unicode表示的str通过 encode() 方法可以编码为指定的bytes：
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii')) 报错，中文编码的范围超出了ASCII的范围
'''
在bytes中，无法显示为ASCII字符的字节，用 \,x## 显示
（因为报错，所以在 \ 和 x 之间加了逗号！！！）
'''

print("""""")

# 2.bytes转str——将从网络或磁盘上读取的bytes类型的字节流转为str，用 decode() 方法：
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
