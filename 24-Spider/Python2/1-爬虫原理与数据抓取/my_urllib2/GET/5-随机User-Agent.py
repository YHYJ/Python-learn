#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""随机 添加/删除 User-Agent"""

import random
import urllib2

from Python2.conf.User_Agent_list import USER_AGENT_LIST


url = "http://yj1516.site"


user_agent = random.choice(USER_AGENT_LIST)

request = urllib2.Request(url)


request.add_header("User-Agent", user_agent)


print request.get_header("User-agent")
