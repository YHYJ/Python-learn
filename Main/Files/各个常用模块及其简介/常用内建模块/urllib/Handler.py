#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""如果需要更复杂的控制，比如通过一个Proxy去访问网站，需要利用ProxyHandler来处理"""


from urllib import request


# 通过一个Proxy访问网站
'''示例代码:'''
proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass
