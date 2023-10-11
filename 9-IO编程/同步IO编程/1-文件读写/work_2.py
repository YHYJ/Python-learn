#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""2、访客名单：
提示用户输入其名字
用户输入名字后在屏幕上打印一句问候语
将访问记录添加到文件 guest_book.txt 中
确保这个文件中的每条记录都独占一行
"""

file_name = './Data/guest_book.txt'
with open(file=file_name,mode='a') as file_object:
    while True:
        name = input("请输入用户名(置空退出):")
        if name == '':  #输入用户名为空，退出循环
            break
        print("欢迎光临：" + name)
        file_object.write(name + "来访\n")