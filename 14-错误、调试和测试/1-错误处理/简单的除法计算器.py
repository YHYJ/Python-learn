#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""处理 ZeroDivisionError 异常"""

"""对一个数进行除0计算将引发 ZeroDivisionError: division by zero 错误,
其中ZeroDivisionError就是一个异常对象
"""

"""使用try-except和else代码块改写除法计算器以规避异常"""

print("*"*25 + "除法计算器" + "*"*25)
print("按‘q’回车退出运行")
while True:
    first_number = input("请输入被除数：")
    if first_number == 'q':
        break
    second_number = input("请输入除数：")
    if second_number == 'q':
        break
    try:                        #尝试执行try代码块，只包含可能引发异常的代码
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:   #如果引发某种异常，执行except代码块
        print("0不能作为被除数!\n")
    else:                       #如果try代码块成功执行，未出现任何异常，执行else代码块
        print(answer,"\n")
    finally:
        print('end'.upper())
#当程序在try内部执行某行代码引发异常时，会直接跳过try中剩下的代码