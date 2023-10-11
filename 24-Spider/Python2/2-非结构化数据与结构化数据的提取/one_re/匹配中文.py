#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""中文的unicode编码范围主要在 [u4e00-u9fa5] 之间（不包括全角标点）"""

import re


title = u"你好，再见"

print(title)
print(type(title))


pattern = re.compile(ur"[\u4e00-\u9fa5]")   # r 表示使用原始字符串，u 表示是 unicode 字符串

zh = pattern.findall(title)

print(zh)
