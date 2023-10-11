#!/usr/bin/env python3
# -*- coding: utf-8 -*-

string = "你我他它蛤234"

# [action:end]
print("*"*35 + "[action:end]" + "*"*35)
print('1、获得一个从string的第0位到最后一位的副本：%s.' % string[:])
print('2、获得一个从string的第0位到最后一位的副本：%s.' % string[:len(string)])


# [action:end:long]
print("*"*35 + "[action:end:long]" + "*"*35)
"""
str[action:end:long] ——
    action —— 从此下标开始切片，默认为0
    end —— 切片到此下标停止（不取b）,默认为len(str)
    long —— 步长，正数代表向右数，负数代表向左数，默认为+1
"""
print('3、获得一个从string的第0位到最后一位的副本：%s' % string[::])
print('4、获得一个string的向后计数的副本，即逆置：%s' % string[::-1])
print('4.1、获得一个string的向后计数的副本，即逆置：', string[len(string)::-1])
print('5、从下标为5处开始倒序取，到下标为1处停止：%s' % string[5:1:-1])
print('6、从下标为1处开始倒序取：%s' % string[1::-1])
