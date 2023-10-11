#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import urllib2

from save_file import save_file
from conf.User_Agent_list import USER_AGENT_LIST


def spider(url, file_name, timeout):
    """
    爬虫主体
    :param url: 待抓取URL
    :param file_name: 存储文件名
    :return:
    """
    print "正在抓取：<{}>\n".format(url)

    user_agent = random.choice(USER_AGENT_LIST)

    headers = {
        "User-Agent": user_agent
    }

    request = urllib2.Request(url, headers=headers)

    try:
        response = urllib2.urlopen(request, timeout=timeout)

        html = response.read()

        save_file(html, file_name)
    except Exception as e:
        print e
