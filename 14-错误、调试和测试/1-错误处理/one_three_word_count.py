#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""分析多个文件"""

def count_words(filename):
    """计算一个文件大致包含多少单词"""
    try:
        with open(file=filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        #mag = "抱歉！当前目录未找到名为 " + filename[7:-4] + " 的文件."
        #print(mag)
        pass    #使用pass使Python在发生异常时不进行提示
    else:
        #计算文件大致包含多少单词
        words = contents.split()
        num_words = len(words)
        print("《" + filename.title()[7:-4] + "》" + "大约包含" + str(num_words) + "个单词.")

files = ['./Data/alice.txt','./Data/moby_dick.txt','./Data/siddhartha.txt','./Data/傲慢与偏见.txt']
for file in files:
    count_words(filename=file)