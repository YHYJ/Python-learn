#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""枚举类型可以看作是一种标签或是一系列常量的集合
通常用于表示某些特定的有限集合，例如星期、月份、状态等"""

"""当需要定义常量时，一个办法是用大写变量通过整数来定义"""
# 例如月份：
JAN = 1
FEB = 2
MAR = 3
'''优点是简单，缺点是类型是int，并且仍然是变量'''


"""更好的方法是为这样的枚举类型定义一个class
然后，每个常量都是class的一个唯一实例"""
from enum import Enum,unique
# Py提供了Enum类来实现这个功能：

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul',
                      'Aug','Sep','Oct','Nov','Dec'))
'''这样就获得了Month类型的枚举类'''
# 可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
for name,member in Month.__members__.items():
    print(name, "=>", member, ",", member.value)    # value属性是自动赋给成员的int常量，默认从1开始


"""如果需要更精确地控制枚举类型"""
# 可以从Enum派生出自定义类：
@unique     # @unique装饰器帮助确保没有重复值
class Weekday(Enum):
    Sun = 0     # Sun的value值设为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fir = 5
    Sat = 6

d1 = Weekday.Mon
print(d1)                # 赋值访问
print(Weekday.Thu)       # 直接访问
print(Weekday['Tue'])    # 名称访问
print(Weekday(2))        # value值访问
print(Weekday.Fir.value) # 获得value
print(d1 == Weekday.Mon) # d1是Mon
print(d1 == Weekday.Wed) # d1不是Wed
print(d1 == Weekday(4))  # d1不是Thu
# print(Weekday(7))        # 不存在7这个value
for name,weekday in Weekday.__members__.items():
    print(name, "=>", weekday, ",", weekday.value)
'''既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量'''

'''Enum可以把一组相关常量定义在一个不可变的class中，成员可以直接比较'''