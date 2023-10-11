#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# 两个常量：
print(math.pi)  # 圆周率π
print(math.e)   # 自然常数e


'''数值运算'''
# 对x向上取整：
print(math.ceil(1.0))
print(math.ceil(1.2))

# 对x向下取整：
print(math.floor(6.0))
print(math.floor(6.9))

# 指数运算：
print(math.pow(6, 3))

# 对数运算，默认基底是e，可以用base参数来改变基底：
print(math.log(100, 10))
print(math.log(1000, 10))    # 为什么是2.9999999999999996 ???

# 平方根：
print(math.sqrt(100))

# 绝对值：
print(math.fabs(-9.1))

# 角度和弧度转换：
# 角度转弧度
print(math.radians(90))
# 弧度转角度
print(math.degrees(1.57))

''''三角函数:
math.sin(x)
math.cos(x)
math.tan(x)
math.asin(x)
math.acos(x)
math.atan(x)'''
