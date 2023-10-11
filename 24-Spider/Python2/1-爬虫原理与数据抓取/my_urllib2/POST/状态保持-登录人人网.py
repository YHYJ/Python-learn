#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib
import urllib2
import cookielib

from plugs_one.save_file import save_file


def login():
    # 1. 构建CookieJar对象来保存cookie
    cookiejar = cookielib.CookieJar()

    # 2. 使用HTTPCookieProcessor()创建cookie处理器对象，参数是cookie
    handler = urllib2.HTTPCookieProcessor(cookiejar)

    # 3. 创建opener
    opener = urllib2.build_opener(handler)

    # 4. 构建headers信息
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64…) Gecko/20100101 Firefox/57.0"
    }

    # 5. URL和用户名密码信息
    login_url = "http://www.renren.com/PLogin.do"
    user_pw = {"email": "mr_mao_hacker@163.com", "password": "alarmchime"}

    # 6. 信息转码
    real_user_pw = urllib.urlencode(user_pw)

    # 7. 构建request
    request = urllib2.Request(login_url, data=real_user_pw, headers=headers)

    # 8. 发送一次请求获取cookie
    opener.open(request)

    # 9. 全局声明opener，以便使用cookie
    urllib2.install_opener(opener)


def after_login():
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64…) Gecko/20100101 Firefox/57.0"
    }

    start_url = [
        "http://www.renren.com/327550029/profile",
        "http://www.renren.com/410043129/profile",
        "http://www.renren.com/403811175/profile"
    ]

    for i, url in enumerate(start_url):
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)

        html = response.read()
        file_name = "抓取人人网数据_{}.html".format(i)

        save_file(html, file_name)


if __name__ == '__main__':
    login()
    after_login()
