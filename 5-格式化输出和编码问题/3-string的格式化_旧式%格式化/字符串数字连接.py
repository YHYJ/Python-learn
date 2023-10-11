#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#======== 将两段字符连起来输出 ========#
str1 = 'good'
str2 = 'bye'
print(str1 + str2)
print('very' + str1 + str2)
#=== 想要把数字接到字符串后面输出时，有两种方法：
#1、用str()把数字转换成字符串
num = 21
print('My age is ' + str(num))
print('My age is ' + str(21))
#2、用%对字符串进行格式化
num = 21
print('My age is %d'%num)  #注意 'My age is %d' 和 % num 之间没有逗号
print('My age is %.1f'%21.8)  #这里 %d 只能用来格式化整数，小数用 %f.(和C一样)
name = 'WangXin'
print('%s is a good teacher.'%name)        #%s代替字符串。%name，name没引号代表变量
print('%s is a good teacher.'%'WangXin')    #也可以这样子，%'WangXin'，'WangXin'有引号代表字符串


#在一个print中打印出学生的姓名和成绩
print("%s's score is %d" %('Mike',98))
#或者
name = 'Lily'
score = 99
print("%s's score is %d" %(name,score))

#('Mike',98)这种用()表示的一组数据在Python中叫做 元组(tuple) ，是Python的一种基本数据结构，常用！！！
