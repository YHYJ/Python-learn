#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构
每个节点都是Python对象,所有对象可以归纳为4种:
    Tag
    NavigableString
    BeautifulSoup
    Comment
"""

from bs4 import BeautifulSoup


html = """
<html><head><title>Title</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, "lxml")

'''1. Tag
就是HTML中的标签
Tag 的两个重要属性：name（标签名）和 attrs（属性）
'''
print("----------1----------")

print(soup.name)    # soup 对象特殊，它的 name 是 [document]
print(type(soup.name))    # 类型 <type 'unicode'>

# 两个重要属性name（标签名）和 attrs（属性）
print(soup.title.name)  # <title> 标签的name
print(soup.p.attrs)     # <p> 标签的所有属性，一个字典
print(soup.p["class"])  # <p> 标签的class属性，一个列表
print(soup.p.get("class"))  # 同上

print(soup.title)   # 输出 <title> 标签及其内容
print(soup.head)    # 输出 <head> 标签及其内容
print(soup.a)       # 输出 <a> 标签及其内容
print(soup.p)       # 输出 <p> 标签及其内容
print(type(soup.p))   # 类型 <class 'bs4.element.Tag'>
'''只查找第一个符合要求的标签'''


'''2. NavigableString
获取标签内部的文字，用 .string 或 .get_text() 方法
'''
print("----------2----------")

print(soup.head.string)    # 第一个 <head> 标签里面的文字，就算里面还有标签也忽略
print(type(soup.head.string))   # 类型 <class 'bs4.element.NavigableString'>

print(soup.head.get_text())  # 同 .string
print(type(soup.head.get_text()))  # 类型 <type 'unicode'>


'''3. BeautifulSoup
BeautifulSoup 对象表示的是一个文档的内容
大部分时候, 可以把它当作一个特殊的 Tag 对象，可以分别获取它的类型，名称
'''
print("----------3----------")
print(soup.name)
print(soup.attrs)   # 文档本身的属性为空 {}


'''4. Comment
一个特殊类型的 NavigableString 对象，输出的内容不包括注释符号
'''
print("----------4----------")
print(soup.a)   # 输出包含注释符号
print(soup.a.string)   # 输出不包含注释符号
print(type(soup.a.string))   # 输出不包含注释符号


"""总结"""
print("----------总结----------")
print(soup.title)            # 指定标签及其内容
print(soup.title.name)       # 指定标签的标签名
print(soup.title.string)     # 指定标签的里纯粹的内容
print(soup.head.get_text())  # 指定标签里的纯粹的内容

print(soup.p.attrs)         # 指定标签的所有属性，前提是该标签有属性
print(soup.p.get("class"))  # 单独获取指定属性
print(soup.p["name"])       # 单独获取指定属性
