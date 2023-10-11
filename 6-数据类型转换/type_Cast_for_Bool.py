#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#======== 在Python中，以下数值会被认为是False,其他值是True ========#
#1、为0的数字
print(bool(0))      #False
print(bool(0.0))    #False

#2、空字符串
print(bool(''))     #False。注意和bool(' ')的区别
print(bool(""))     #False

#3、表示空值的None——（None是Python中的一个特殊值，表示什么都没有，它和0、空字符、False、空集合都不一样）
print(bool(None))   #False

#4、空集合
print(bool())       #False
print(bool([]))     #False
print(bool({}))     #False

print('''''')

#======== 在if、while等条件判断语句里，判断条件会自动进行一次bool的转换 ========#
a = '1230'
if a:
    print('This is not a blank string!')
#=== 效果等同于：
if bool(a):
    print('This is not a blank string!*2')
if a != '':
    print('This is not a blank string!*3')
