#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
split ——把字符串转成list
join ——把list转成字符串，join不是list的方法，而是字符串的方法
"""


mystr = '12, CDVS 2c'

# split()
'''把字符串转成list,
list()方法是把字符串里的每个字符都作为list里的一个元素
split()把字符串里的每个子串作为一个元素'''
print(mystr.split())
print(list(mystr))


I = ['hello', '你好']      # list中的元素是字符串时才能用join进行连接

# join()
"""首先需要一个额外的字符串作为list中所有元素的连接符
然后再调用这个连接符的join方法，join的参数是被连接的list"""
s = '-'     # 定义一个字符串作为连接符
LI = s.join(I)
print(LI)
'''也可以在输出的时候直接用一个字符串作为连接符'''
print('+'.join(I))
'''用来作为连接符的字符串可以是一或多个字符，也可以是一个空串'''
print(''.join(I))

print(type(str(I)), str(I))  # str()也能将列表转换成字符串类型，但看起来还是列表
print(type(repr(I)), repr(I))  # repr()也能将列表转换成字符串类型，但看起来还是列表
