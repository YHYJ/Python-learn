#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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


"""1. 直接子节点：.contents  .children 属性"""
print("----------1----------")
'''.contents
tag 的 .contents 属性可以将tag的子节点以列表的方式输出
可以用列表索引来获取它的某一个元素'''
print(soup.html.contents)
print(soup.html.contents[0])

'''.children
返回一个list迭代器对象'''
print(soup.html.children)
print(type(soup.html.children))  # 列表迭代器对象
for child in soup.html.children:
    '''大约可以用来格式化html'''
    print(child)


"""2. 所有子孙节点：.descendants 属性
可以对所有tag的子孙节点进行递归循环，需要遍历获取其中内容
"""
print("----------2----------")
for desc in soup.descendants:
    print(desc)
