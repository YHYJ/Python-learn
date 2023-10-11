#!/usr/bin/env python3
# -*- coding: utf-8 -*-


file_path = './Data/programming.txt'


print("*"*25 + "单行写入" + "*"*25)

# 写入空文件，没有该文件的话会自动创建
with open(file=file_path,mode='w',encoding='gbk') as file_object:
    file_object.write("在漫天风沙里，望着你远去，我竟悲伤的不能自已\n")   # 多行写入加换行符
    file_object.write('1516\n')
    file_object.write('QQ:' + str(1339670004) + "\n")   # write的参数只能是str变量


with open(file=file_path,mode='a',encoding='gbk') as file_object:  # 附加模式
    file_object.write("是谁来自山川湖海，却囿于厨房、昼夜与爱\n")
    file_object.write("十年饮冰，难凉热血\n")