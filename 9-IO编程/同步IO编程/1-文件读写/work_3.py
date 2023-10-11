#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""3、调查：
询问用户为何喜欢编程
每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中
"""

file_name = './Data/reason.txt'
values = 1
with open(file=file_name,mode='a') as file_object:
    question = "请问你为何喜欢小猫："
    file_object.write(question + "\n")
    while values < 4:
        print(question)
        if values < 4:
            reason = input("请输入你的答案：")
        file_object.write(str(values) + "." + str(reason) + "\n")
        values += 1