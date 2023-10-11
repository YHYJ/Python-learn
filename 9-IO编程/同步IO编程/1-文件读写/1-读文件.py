#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符）
然后通过操作系统提供的接口对文件进行操作"""


"""读取全部内容：
以读文件的模式打开./Data/pi_digits.txt 文件对象并读取全部内容"""
# ——> file_reader.py
'''打开文件默认是'r'读模式，所以可以省略标识符'''


"""逐行读取文件：
逐行读取可以在文件中查找特定的信息，或者以某种方式修改文件中的文本
以读文件的模式打开./Data/pi_digits.txt 文件对象并逐行读取文件"""
# 要以每次一行的方式检查文件，可对文件对象使用for循环 ——> file_readerline.py
'''
read()          一次性读取文件的全部内容        在文件很小时调用
read(num)       每次最多读取num个字节的内容     在不能确定文件大小时调用
readline()      可以每次读取一行内容
readlines()     一次读取所有内容并按行返回list   配置文件调用readlines()
'''


"""创建一个包含文件各行内容的列表：
使用关键字with时， open()返回的文件对象只在with代码块内可用
要在with代码块外访问文件的内容:
    可在with代码块内将文件的各行存储在一个列表中
这样可以立即处理文件的各个部分，也可推迟到程序后面再处理"""
# 在with中将文件的各行存储在一个列表中，在with外打印 ——> file_readerline.py


"""使用文件中的内容:
将文件读取到内存中后，就可以以任何方式使用这些数据了"""
# 创建一个字符串，包含文件中存储的所有数字，且没有任何空格 ——> pi_string.py
# 检查文件中是否包含某个字符串 ——> pi_string.py


"""file-like Object：
像open()函数返回的这种有个read()方法的对象，Py统称为file-like Object
除了file外，还可以是内存的字节流，网络流，自定义流等等
file-like Object不要求从特定类继承，只要写个read()方法就行
StringIO就是在内存中创建的file-like Object，常用作临时缓冲
"""


"""读取二进制文件：
默认是读取文本文件，并且是UTF-8编码的文本文件
要读取二进制文件，用标识符'rb'模式打开文件即可，输出的是十六进制表示的字节"""
# 读取二进制文件(图片、视频等) ——> B_file_reader.py


"""字符编码：
要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数"""
# 例如读取GBK编码的文件：
# f = open('gbk.txt', encoding='gbk')
'''遇到有些编码不规范的文件，可能会遇到UnicodeDecodeError
因为在文本文件中可能夹杂了一些非法编码的字符
这种情况下给open()函数一个errors参数，表示如果遇到编码错误后如何处理'''
# 最简单的方式是直接忽略：
f = open('./Data/1516.txt', encoding='gbk', errors='ignore')
fi = f.readlines()
print(type(fi))