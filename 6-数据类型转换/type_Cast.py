#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python在定义一个变量时不需要对变量的数据类型进行限定，变量会根据赋给它的值自动决定它的类型，也可以在程序中改变它的值和数据类型：
a = 1
print(a)
a = 'hello'
print(a)
a = True
print(a)
#变量a先后是整数，字符串，布尔类型


#虽然类型可也任意改变，但是当对一个特定类型的变量进行操作时，如果这个操作与它的数据类型不匹配，就会产生错误
#print('hello' + 1)  #是错误的，‘hello’是字符串，1 是整数，不能相加
print('hello' + str(23333)) #将23333的数据类型转换成string字符串
print()
#print('hello %d' %'123456') #%d需要的是一个整数，而‘123456’是字符串
print('hello %d' %int('123456'))    #强制‘123456’转换成int类型

print(bool('0'))
