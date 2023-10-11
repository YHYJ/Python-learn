#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""把list里的元素通过一个连接符转换成一个大字符串"""


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
print(' +- '.join(I))
print(''.join(I))
print(' '.join(I))


l = ['www 123']
print(l)
li = ''.join(l)
print(type(li), li)