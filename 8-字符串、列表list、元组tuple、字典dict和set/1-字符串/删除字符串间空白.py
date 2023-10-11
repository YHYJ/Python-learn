#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Py认为字符串间的空白是有意义的.
Py能够识别字符串开头和末尾多余的空白
删除操作的结果是原字符串的拷贝"""


favorite_language = ' |language python| '
print('空白->|'+favorite_language+'|<-空白')

# lstrip()
'''删除左端空格'''
favorite = favorite_language.lstrip()
print('左端：', '空白->|'+favorite+'|<-空白')


# rstrip()
'''删除右端空格'''
favorite = favorite_language.rstrip()
print('右端：', '空白->|'+favorite+'|<-空白')


# strip()
'''删除两端空格'''
favorite = favorite_language.strip()
print('两端：', '空白->|'+favorite+'|<-空白')


# 指定要去除的字符串
'''默认去除空格，也可以去除其他字符串'''
x = 'xzhy 123djhk zxcydn zx'
print(x.lstrip('xyz'))
print(x.rstrip('xyz'))
print(x.strip('xyz'))
'''在左右查找指定的字符串，删除到非指定字符串为止'''
