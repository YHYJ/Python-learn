#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""urllib提供了一系列用于操作URL的功能"""


from urllib import request


# Get——request模块
'''urllib的request模块可以非常方便地抓取URL内容
也就是发送一个GET请求到指定的页面，然后返回HTTP的响应
例如，对豆瓣的一个URL 
https://api.douban.com/v2/book/2129650进行抓取，并返回响应'''
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('状态：', f.status, f.reason)
    for k, v in f.getheaders():
        print('头数据：%s: %s' %(k, v))
    print('数据：', data.decode('utf-8'))

print('\n', '*'*100, '\n')

# 模拟浏览器发送GET请求——Request对象
'''通过往Request对象添加HTTP头，可以把请求伪装成浏览器
例如，模拟iPhone 6去请求豆瓣首页'''
req = request.Request('https://www.douban.com/')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
               'AppleWebKit/536.26 (KHTML, like Gecko) '
               'Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('状态：', f.status, f.reason)
    for k, v in f.getheaders():
        print('头数据：%s: %s' % (k, v))
    print('数据：', f.read().decode('utf-8'))
