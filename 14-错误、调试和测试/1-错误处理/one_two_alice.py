#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""处理 FileNotFoundError 异常"""
'''
file_name = 'alice.txt'
with open(file=file_name) as f_obj:
    contents = f_obj.read()
将引发 FileNotFoundError 异常：找不到文件
'''


"""改写——使用try-except代码块"""
#
file_name = 'alice.txt'
try:
    with open(file=file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    mag = "抱歉！当前目录未找到名为 " +\
          "《" + file_name.title()[:-4] + "》" + " 的文件."
    print(mag)


"""拓展——分析文本"""
#方法split()以字符串中的空格将字符串分拆成多个部分，并将这些部分都存储到一个列表中
#对整篇文本调用split()，再计算得到的列表包含多少个元素，从而确定整篇文本大致包含多少个单词
file_name = './Data/alice.txt'
try:
    with open(file=file_name) as f_obj:
        contents = f_obj.read()     #现在是一个超长字符串，好汉alice.txt的全部文本
except FileNotFoundError:
    mag = "抱歉！未找到名为 " + "《" + file_name.title()[7:-4] + "》" + " 的文件."
    print(mag)
else:
    #计算文件大只包含多少单词
    words = contents.split()    #调用split()方法，以生成一个列表，其中包含这部童话中的所有单词
    num_words = len(words)      #计算这个列表的长度
    print("《" + file_name.title()[7:-4] + "》" + "大约包含" +
          str(num_words) + "个单词.")