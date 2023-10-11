#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""在Py中使用正则表达式时，re模块内部会干两件事情：
1、编译正则表达式，如果正则表达式的字符串本身不合法，会报错
2、用编译后的正则表达式去匹配字符串"""


import re

# 可以预编译正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
'''编译:'''
re_telephon = re.compile(r'^(\d{3})-(\d{3,8})$')
'''使用:'''
print(re_telephon.match('010-151626').groups())
print(re_telephon.match('010-8086').groups())
'''编译后生成Regular Expression对象
由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串'''
