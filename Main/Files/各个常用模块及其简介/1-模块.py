#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python自带了功能丰富的标准库，另外还有数量庞大的各种第三方库。
使用这些库将使开发事半功倍——‘拼车轮’

使用这些功能的基本方法是使用 模块 。
通过函数，可以在程序里复用代码；通过模块，则可以重用别的程序中的代码。

【模块】 可以理解为是一个包含了函数和变量的py文件。在你的程序中引入了某个模块，就可以使用其中的函数和变量
"""


#之前使用过的模块：
#   import random
#import语句告诉Python，我们要用random模块中的内容。然后就可以使用random中的方法，比如：
#   random.randint(0,10)
#   random.choice([1,3,5])
'''注意！！！函数前需要加上调用的模块的名字！！！！！！！！！'''


#想知道random中有哪些函数和变量，可以用dir(random)
import random
print(dir(random))
print()

import math
print(dir(math))
print()


#如果只是用到random中的某一个函数或变量，也可以通过       from……(模块名)……import……(函数或变量名)……     指明：
from math import pi
print('pi=',pi)
print()


#为了便于理解和避免冲突，可以给引入的方法换个名字：
from math import pi as math_pi
print('math_pi=',math_pi)
print()