#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


# 一. 基本POST请求
def youdao():
    word = raw_input("查询词：")
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    data = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false",
    }

    response = requests.post(url, data=data, headers=headers)
    # print(response.text)
    # print(response.content)
    print(response.json())


if __name__ == '__main__':
    youdao()
