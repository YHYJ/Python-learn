#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""让用户选择何时退出"""


prompt = "Tell me st,and i will repeat it back to you,"
prompt += "\nEnter ’quit‘ to end the program:"
active = True
while active:
    message = input(prompt)

    if message == 'quit':   # 检查输入，仅在不是 'quit' 时打印输入
        active = False
    else:
        print(message)


print("*"*25 + "使用标志" + "*"*25)

'''使用标志.

在要求很多条件都满足才继续运行的程序中，定义一个变量
用于判断整个程序是否处于活动状态，，这个标量叫做　标志　.'''
age = "婚龄查询系统."
age += "\n请输入你的年龄:"
value = True
while value:
    query = float(input(age))

    if query >= 20:
        print("达到法定结婚年龄\n")
    elif query < 20 and query >= 18:
        print("尚未达到法定结婚年龄\n")
    elif query < 18 and query > 0:
        print("尚未成年\n")
    else:
        print("请输入正确年龄\n")
        value = False


print("*"*25 + "使用break退出循环" + "*"*25)

'''break语句用于控制程序流程.

可使用它来控制哪些代码行将执行，哪些代码行不执行，从而让程序按要求执行代码.
'''
city = "Please enter the name of a city you have visited:"
city += "\n(Enter 'quit' when you finished.)"
while True:
    IO = input(city)

    if IO == 'quit':
        break
    else:
        print("I'd love to go to " + IO.title() + "!\n")


print("*"*25 + "使用continue重启循环" + "*"*25)

'''continue语句要返回到循环开头.

并根据条件测试结果决定是否继续执行循环.
'''
number = 0
while number < 10:
    number += 1
    if number % 2 != 0:     # 如果number对取余结果不为0
        continue    # 就忽略下面的代码
    print(number)   # 如果if语句不成立，打印对２取余等于0的number
