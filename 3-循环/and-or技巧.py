#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = "heaven"
b = "hell"
c = True and a or b
print('c=', c)
d = False and a or b
print('d=', d)


""""
表达式从左往右运算，1和"heaven"做and的结果是"heaven"，再与"hell"做or的结果是"heaven"；
0和"heaven"做and的结果是0，再与"hell"做or的结果是"hell"。
在一个bool and a or b语句中，当bool条件为真时，结果是a；当bool条件为假时，结果是b
"""

# 有了它，原本需要一个if-else语句表述的逻辑：
A = -6
if A > 0:
    print("big")
else:
    print("small")

# 就可以直接写成：
print((A > 0) and "big" or "small")
'''
然而，和c语言中的?:表达式不同，这里的and or语句是利用了python中的逻辑运算实现的。
当a本身是个假值（如0，""）时，结果就不会像期望的那样
'''
# 比如：
a = ""
b = "hell"
c = True and a or b
print('c=', c)

# 得到的结果不是""而是"hell"。因为""和"hell"做or的结果是"hell"

"""
所以，and-or真正的技巧在于，确保a的值不会为假。
"""
a = ""
b = "hell"
c = (True and [a] or [b])
# 最常用的方式是使 a 成为 [a]、b 成为 [b]，然后使用返回值列表的第一个元素————[0]
print('c=', c)
# 由于[a]是一个非空列表，所以它绝不会为假
# 即使a是0或者''或者其它假值，列表[a]也为真，因为它有一个元素

'''在两个常量值进行选择时，and-or会让你的代码更简单'''
