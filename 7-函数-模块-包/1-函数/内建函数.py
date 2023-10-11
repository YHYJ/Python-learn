#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
#>>> a = abs # 变量a指向abs函数
#>>> a(-1) # 所以也可以通过a调用abs函数
1
"""

# --** isinstance() 数据类型检查！！检查赋给参数的值是否符合参数的数据类型
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(16))

print('--------------------')



# --** abs() 求绝对值
print(abs(-5))


# --** max() 求多个数的最大值
print(max(1,-2,0,12.5))


# --** 数据类型转换————int() ; str() ; float() ; bool()
print(type(int('1516')),int('1516'))
print(type(int(15.16)),int(15.16))
print(type(str(1516)),str(1516))
print(type(float(1516)),float(1516))
print(type(float('1516')),float('1516'))
print(type(bool('1516')),bool('1516'))
print(type(bool()),bool())
print(type(bool()),bool(1))


# --** hex() 转换为十六进制
print(hex(100))