#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random
import urllib
import urllib2

from conf.User_Agent_list import USER_AGENT_LIST


def youdao_fanyi():
    """
    有道翻译
    :return:
    """
    word = raw_input("开始查询：")
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    formdata = {
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
    real_form = urllib.urlencode(formdata)

    user_agent = random.choice(USER_AGENT_LIST)

    headers = {
        "User-Agent": user_agent
    }

    request = urllib2.Request(url, data=real_form, headers=headers)

    response = urllib2.urlopen(request)

    # 获得响应，格式为JSON字符串，转为Python数据格式

    json_str = response.read()
    dict_data = json.loads(json_str)

    print "查询结果：{}".format(dict_data["translateResult"][0][0]['tgt'])


if __name__ == '__main__':
    youdao_fanyi()
