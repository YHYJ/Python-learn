#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""检查字符串中是否包含某个子串"""


mystr = "hello world it's and me"

# find()和rfind()
print('*'*25, 'find()和rfind()', '*'*25)
'''返回字符串中第一个'it'子串的索引，如果没有该子串就返回-1'''
print(mystr.find('it'))
print(mystr.find(",it's"))
print(mystr.rfind('it'))    # 从右开始查找'it'
'''rfind()类似于find()，不过是从右边开始查找，但返回的索引还是最左为0'''


# index()和rindex()
print('*'*25, 'index()和rindex()', '*'*25)
'''跟find()方法一样，只不过如果str不在 mystr中会报一个异常'''
print(mystr.index('it', 0, len(mystr)))
# print(mystr.index('its', 0, len(mystr)))
print(mystr.rindex('it', 0, len(mystr)))
'''rindex()类似于index()，不过是从右边开始查找，但返回的索引还是最左为0'''

mystr.strip()
# count()
print('*'*25, 'count()', '*'*25)
'''返回mystr里str在start和end之间出现的次数'''
print(mystr.count('it', 0, len(mystr)))
print(mystr.count("it's", 0, len(mystr)))


# 判断字符串的组成元素
print('*'*25, "判断字符串的组成元素", '*'*25)
# isalpha() ——判断字符串是否由纯字母组成
print('abc'.isalpha())
print('abc '.isalpha())
# isdecimal() ——判断字符串是否由纯unicode十进制数组成
print('123'.isdecimal())
print('123a'.isdecimal())
# isspace() ——判断字符串是否由纯空格组成
print('  '.isspace())
print(' .'.isspace())
# isdigit() ——判断字符串是否由纯数字组成
print('123'.isdigit())
print('123 '.isdigit())
# isalnum() ——判断字符串是否由字母或数字或两者组成
print('123'.isalnum())
print('abc'.isalnum())
print('123abc'.isalnum())


# 检查字符串从开头或结尾是否有某个特定子串
print('*'*25, "检查字符串是否以某个特定子串开头或结尾", '*'*25)
print(mystr.startswith('hello w'))  # 开头是否有某个子串
print(mystr.endswith("t's"))    # 结尾是否有某个子串
