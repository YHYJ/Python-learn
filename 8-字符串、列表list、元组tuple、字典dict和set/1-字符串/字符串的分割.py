#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""想要对网页上的链接进行自动抓取等等，需要对代码进行处理
处理过程中就要在字符串和list之间进行操作
比如一个英语句子，需要对这个句子每个单词进行单独处理
就需要对字符串进行分割"""


sentence = "I'm \nan English an sentence"

# split()和splitines()
print('*'*25, "split()和splitines()", '*'*25)
'''以一个str为分割符切片mystr
如果参数maxsplit指定，则仅分割出maxsplit个子字符串
余下的字符串不论多长都是一个'''
print(sentence.split(' '))
print(sentence.split(' ', maxsplit=3))
print(sentence.splitlines())    # 按行分隔，返回一个包含各行作为元素的列表


# partition()和rpartition()
print('*'*25, "partition()和rpartition()", '*'*25)
'''将字符串按某个子串分割成前、本身、后三部分'''
print(sentence.partition('an'))
print(sentence.rpartition('an'))    # 类似于 partition(),不过是从右边开始


# （面试题）给定一个字符串aStr，返回使用空格或者'\t'分割后的倒数第二个子串
ss = 'haha nihao a \t heihei \t woshi nide \t hao \npengyou'
print(ss)
print(ss.split())
print(ss.split()[-2])
