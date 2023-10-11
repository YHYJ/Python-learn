#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
lxml 是 一个HTML/XML的解析器，主要的功能是解析和提取 HTML/XML 数据。
lxml 和正则一样，也是用 C 实现的，是一款高性能的 Python HTML/XML 解析器，可以利用XPath语法，来快速的定位特定元素以及节点信息。
lxml python 官方文档：http://lxml.de/index.html
"""

from lxml import etree


"""读取字符串"""
# 注意，第五个li标签缺少闭合标签
text = """
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
"""

'''利用etree.HTML将字符串解析为HTML文档'''
html = etree.HTML(text)

'''按字符串序列化HTML文档'''
result = etree.tostring(html)

print(result)
'''lxml 可以自动修正 html 代码，例子里不仅补全了 li 标签
还添加了 body，html 标签'''


"""读取文件"""
html_file = etree.parse("./hello.html")
result_file = etree.tostring(html_file)

print(result_file)
