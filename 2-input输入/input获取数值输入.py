#!/usr/bin/env python3
# -*- coding: utf-8 -*-


age = input("How old are you:")     # 使用函数input()时，默认输入的是字符串类型
print(type(age), age)


'''将输入转换为数值类型'''
ages = input("How old are you:")
ages = int(ages)    # int()转换
print(type(ages), ages)


c = input('请输入c的值：')
d = input('请输入d的值：')
a = c + d
print('c+d=', a)
