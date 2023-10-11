#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""有些Web服务器（包括HTTP/FTP等）的有些页面并不想提供公共访问权限，或者某些页面不希望公开
但是可以让特定的客户端访问。那么会在用户访问时要求进行身份认证
爬虫直接访问会报HTTP 401 错误，表示访问身份未经授权：
    urllib2.HTTPError: HTTP Error 401: Unauthorized

HTTPPasswordMgrWithDefaultRealm()类将创建一个密码管理对象，用来保存 HTTP 请求相关的用户名和密码，主要应用两个场景：
    1. 验证代理授权的用户名和密码 (ProxyBasicAuthHandler())
    2. 验证Web客户端的的用户名和密码 (HTTPBasicAuthHandler())

ProxyBasicAuthHandler(代理授权验证)
如果使用之前的代码来使用私密代理，会报 HTTP 407 错误，表示代理没有通过身份验证：
    urllib2.HTTPError: HTTP Error 407: Proxy Authentication Required
改写代码，通过：
    1. HTTPPasswordMgrWithDefaultRealm()：来保存私密代理的用户密码
    2. ProxyBasicAuthHandler()：来处理代理的身份验证。
"""

import urllib2


def send_request():
    username = "bigcat"
    password = "123456"
    url = "http://192.168.93.57"

    # 1.创建一个密码管理器对象，用来保存和HTTP请求相关的账户密码信息
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # 2. 添加账户密码信息，分别表示域服务器信息（一般写None），服务器url，账户名，密码
    password_mgr.add_password(None, url, username, password)

    # 3. 构建一个HTTP web 验证的处理器对象，构建自定义opener对象，发送请求即可
    auth_handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(auth_handler)
    response = opener.open(url)

    print response.read()


if __name__ == "__main__":
    send_request()
