#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
格式
lambda 参数1,参数2,参数3,…: 返回值
"""


'''无参数'''
# 如果没有参数，则lambda冒号前面就没有，如：
print(lambda:'beginman')    # 这样只是简单的用lambda创建了一个函数对象，并没有保存和调用它，时刻会被回收
bar = lambda :'beginman'    # 创建、保存并调用
print(bar())

'''有参数'''
def sum(x,y=10):
	return x+y
print(sum(1))
print(sum(1,100))

sum2 = lambda x, y=10:x+y
print(sum2(1))
print(sum2(1,100))


"""lambda与def"""
# 1.lambda函数只是创建简单的函数对象，是一个函数的单行版本，但是由于lambda调用的时候绕过函数的栈分配，所以性能有所增强
# 2.lambda会创建一个函数对象，但不会把这个函数对象赋给一个标识符，而def则会把函数对象赋值给一个变量——匿名实名的区别
# 3.lambda只是一个表达式，而def则是一个语句。lambda表达式运行起来像一个函数，当被调用时创建一个函数对象


"""lambda函数的用途和注意事项"""
# 1.对于单行函数，使用lambda可以省去定义函数的过程，让代码更加精简
# 2.在非多次调用的函数的情况下，lambda表达式即用既得，提高性能

# 注意：如果for..in..if能做的，最好不要选择lambda
