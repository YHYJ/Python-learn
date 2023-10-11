#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup


html = """
<html><head><title>Title</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.
</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, "lxml")


"""1. find_all(name, attrs={}, recursive=True, text=None, **kwargs)
BeautifulSoup最常用的匹配方法，用来匹配文本中所有符合匹配规则的数据，返回列表
'''
:param attrs: 
:param recursive: 
'''
"""
print("------------name参数------------")
'''
:param name: 指定被匹配的标签名
'''
# 传字符串
print(soup.find_all("p"))
# 传正则
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# 传列表
print(soup.find_all(["a", "b"]))

print("------------text参数------------")
'''
:param text: 搜索文档中的字符串内容
'''
# 传字符串
print(soup.find_all(text="Title"))
# 传正则
print(soup.find_all(text=re.compile(r"Dormouse")))
# 传列表
print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))

print("------------text参数------------")
'''
:param kwargs: 
'''
print(soup.find_all(id='link2'))
print(soup.find_all(id=True))
# Python中的class属于关键字，所以在find_all中使用 class_ 来表示HTML class属性。
print(soup.find_all(class_="sister"))


"""2. find(name=None, attrs={}, recursive=True, text=None, **kwargs):
用法与find_all一样，find返回第一个符合匹配结果
find_all返回所有匹配结果的列表
"""


"""3. CSS选择器
返回所有匹配结果的列表
写 CSS 时，标签名不加任何修饰，类名前加.，id名前加#
也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是list
"""
print("------------通过标签名查找------------")
'''（1）通过标签名查找'''
print(soup.select('title'))
print(soup.select('a'))

print("------------通过类名查找------------")
'''（2）通过类名查找'''
print(soup.select('.sister'))

print("------------通过 id 名查找------------")
'''（3）通过 id 名查找'''
print(soup.select('#link1'))

print("------------组合查找------------")
'''（4）组合查找'''
print soup.select('p #link1')   # <p> 标签下，id=link1的内容
print soup.select("head > title")   # <head> 标签的子标签 <title>

print("------------属性查找------------")
'''（5）属性查找'''
print soup.select('a[class="sister"]')  # class属性是"sister"的 <a> 标签
print soup.select('a[href="http://example.com/elsie"]')  # href属性是"..."的 <a> 标签
print soup.select('p a[href="http://example.com/elsie"]')   # 与别的查找方式组合，不同节点的空格隔离

print("------------获取内容------------")
'''（6）获取内容'''
for title in soup.select('title'):
    print title.get_text()
