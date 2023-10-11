#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib2


url = "http://yj1516.site"

request = urllib2.Request(url)


# 通过调用Request.add_header()添加/修改一个特定的header
request.add_header("User-Agent", "Chrome 59.9")
request.add_header("Connection", "keep-alive")
request.add_header("Accept", "*/*")


# 调用Request.get_header()查看header信息
'''get_header()的字符串参数，第一个字母大写，后面的全部小写'''
User_Agent = request.get_header(header_name="User-agent")
Connection = request.get_header(header_name="Connection")
Accept = request.get_header(header_name="Accept")

response = urllib2.urlopen(request)

html = response.read()

print "header信息：\n" \
      "    User-Agent<{}>\n" \
      "    Connection<{}>\n" \
      "    Accept<{}>".format(User_Agent, Connection, Accept)

# print html
