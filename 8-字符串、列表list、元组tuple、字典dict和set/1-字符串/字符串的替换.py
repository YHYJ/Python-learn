#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""


mystr = "hello world 121 121"

# replace()
'''把mystr中的str1替换成str2,默认全部替换,如果指定参数count，则替换不超过count次'''
print(mystr.replace("1", "二三", 2))
print(mystr.replace("12", "二三", 2))
print(mystr.replace("121", "二三", 1))
