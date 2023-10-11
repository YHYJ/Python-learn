#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""函数可以返回任何类型的值（包括列表和字典等）.
函数执行完毕也没有return语句时，自动return None
return语句将值返回到调用函数的代码行,返回值将程序的大部分工作移到函数中完成，从而简化主程序.
"""

import math


# 比如在游戏中经常需要从一个点移动到另一个点
'''给出坐标、位移和角度，就可以计算出新的坐标'''
def move(x, y, step, angle=0.0):  # step——位移  angle——角度
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
'''然后就可以同时获得2个返回值'''
NX, NY = move(100, 100, 60, math.pi / 6)
print("NY = %f" % NX + "\n" + "NY = %.1f" % NY)

# 但其实这只是一种假象，Python函数返回的是一个元组：
XY = move(100, 100, 60, math.pi / 6)
print(XY)
# 在语法上，返回一个tuple可以省略括号，n个变量可以同时接收一个包含n个元素的元组，
# 并按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个元组，但写起来更方便。

def build_person(first_name,last_name,age = ''):   #接受名和姓
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first':first_name,'last':last_name}  #封装到字典中
    if age:
        person['age'] = age
    return person   # 返回表示人的整个字典
musician = build_person('jimi','hendrix',18)
print(musician)