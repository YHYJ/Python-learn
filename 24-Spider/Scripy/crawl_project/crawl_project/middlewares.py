# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random

from crawl_project.settings import proxy
from crawl_project.settings import USER_AGENT_LIST


class UserAgentMiddleware(object):
    """User-Agent中间件"""
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        request.headers["User-Agent"] = user_agent


class ProxyMiddleware(object):
    """代理中间件"""
    def process_request(self, request, spider):
        request.meta["proxy"] = proxy
