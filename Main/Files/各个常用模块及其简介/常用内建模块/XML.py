#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""操作XML有两种方法：DOM和SAX
DOM把整个XML读入内存解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点
SAX是流模式，边读边解析，占用内存小，解析快，缺点是需要自己处理事件
正常情况下，优先考虑SAX，DOM因为实在太占内存"""


from xml.parsers.expat import ParserCreate


# DOM与SAX
'''Py中使用SAX解析XML非常简洁
通常关心的事件是start_element，end_element和char_data
准备好这3个函数就可以解析XML了'''
# 当SAX解析器读到一个节点 <a href="/">python</a> 时：
'''会产生3个事件：
1、START_ELEMENT事件，读取在<a href="/"时
2、char_data事件，读取在python时
3、END_ELEMENT事件，读取在</a>时'''
# 代码验证
class DefaultSaxHander:

    def start_element(self, name, attrs):
        print('SAX:开始元素: %s, attes: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('SAX:结束元素: %s' % name)

    def char_data(self, text):
        print('SAX:字符元素: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHander()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
'''需要注意的是，读取一大段字符串时，CharacterDataHandler可能被多次调用
所以需要自己保存起来，在EndElementHandler里面再合并'''


# 生成XML
'''最简单也是最有效的生成XML的方法是拼接字符串'''
'''
L = []
L.append(r'</?xml version="1.0"?>')
L.append(r'<root>')
L.append(encode('some & date'))
L.append(r'</root>')
return ''.join(L)
'''


"""小结
解析XML时，注意找出自己感兴趣的节点
响应事件时，把节点数据保存起来。解析完毕后，就可以处理数据
"""