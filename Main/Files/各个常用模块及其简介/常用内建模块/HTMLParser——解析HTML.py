#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""HTML本质上是XML的子集
但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML
"""


from html.parser import HTMLParser
from html.entities import name2codepoint


# HTMLParser ——解析HTML
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s' % name)

    def handle_charref(self, name):
        print('&#%S' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head>嘻嘻</head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')