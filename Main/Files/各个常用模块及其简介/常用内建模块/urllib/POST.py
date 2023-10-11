#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""如果要以POST发送一个请求，只需要把参数data以bytes形式传入"""


from urllib import request, parse


# POST——
'''模拟一个微博登录
先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式-
-以username=xxx&password=xxx的编码传入'''
print('登录weibo.cn...')
mobile = input('请输入手机号：')
passwd = input('请输入密码：')
login_data = parse.urlencode([
    ('username', mobile),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req_1 = request.Request('https://passport.weibo.cn/sso/login')
req_1.add_header('Origin', 'https://passport.weibo.cn')
req_1.add_header('User-Agent',
               'Mozilla/6.0 '
               '(iPhone; CPU iPhone OS 9_0 like Mac OS X) '
               'AppleWebKit/536.26 (KHTML, like Gecko) '
               'Version/8.0 Mobile/10A5376e Safari/8536.25')
req_1.add_header('Referer',
               'https://passport.weibo.cn/signin/login?entry=mweibo'
               '&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req_1, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
