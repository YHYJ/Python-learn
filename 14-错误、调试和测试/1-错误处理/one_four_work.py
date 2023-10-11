#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""work for Error"""

"""加法运算：

提示用户提供数值输入时，常出现用户提供的是文本而不是数字这种情况，
当你尝试将输入转换为整数时，将引发 TypeError 异常.
编写一个程序，提示用户输入两个数字，将它们相加并打印结果.
在用户输入的任何一个值不是数字时都捕获 TypeError 异常,并打印一条友好的错误消息
"""
print("*"*25 + "加法运算" + "*"*25)
#
while True:
        first_num = input("请输入第一个数字：")
        if first_num == 'q':
            break
        second_num = input("请输入第二个数字：")
        if second_num == 'q':
            break
        try:
            result = int(first_num) + int(second_num)
        except ValueError:
            print("请正确输入数字")
        else:
            print(first_num,"+",second_num,"=",result)


"""猫和狗：

在cats.txt中至少存储三只猫的名字，在dogs.txt中至少存储三条狗的名字.
尝试读取这些文件，并将其内容打印到屏幕上.
将这些代码放在一个 try-except 代码块中，以便在文件不存在时捕获 FileNotFound 错误,
并打印一条友好的消息.
"""
print("*"*25 + "猫和狗" + "*"*25)
#
def cd(file_path):
    try:
        with open(file=file_path) as f_obj:
            animal = f_obj.read()
    except FileNotFoundError:
        print("未找到猫/狗记录文件")
    else:
        print("我家有%d种猫/狗:\n" % len(animal.split()) + animal)

cd(file_path='./Data/dogs.txt')


"""常见单词：

使用方法 count() 来确定 'the' 在 'Marriage as a Trade.txt' 中出现了多少次,不论大小写.
"""
print("*"*25 + "查找某个字符串在另一个字符串中出现的次数" + "*"*25)
#
def book_data(book_name,value='the'):
    try:
        with open(file=book_name) as books:
            book = books.read()
    except FileNotFoundError:
        print("未找到文件" + book_name.title()[7:-4])
    else:
        number = book.lower().count(value)
        print("《" + book_name.title()[7:-4] + "》" +
              " 中有 '" + value + "' " +  str(number) + " 个.")

book_data(book_name='./Data/Marriage as a Trade.txt',value='th')