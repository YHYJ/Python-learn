#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""work for 重构"""

"""喜欢的数字：

编写一个程序，提示用户输入喜欢的数字，并使用json.dump()将这个数字存储到文件中.
再编写一个程序，从文件中读取这个值，并打印这个数字（适当修饰）.
”"""
import json

file_path = './Data/work1.json'

try:
    with open(file=file_path) as f_obj:
        number = json.load(f_obj)
except FileNotFoundError:
    number = input("请输入你最喜欢的数字：")
    with open(file=file_path,mode='w') as f_obj:
        json.dump(number,f_obj)
        print("这个数字是:" + number)
else:
    print("这个数字是:" + number)