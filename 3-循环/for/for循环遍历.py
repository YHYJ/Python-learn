#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""for循环是一种遍历列表的有效方式.
但在for循环中不应修改列表，否则将导致Python难以跟踪其中的元素.
"""


classmates = {'小明': 100, '小红': 95, '李雷': 90, '韩梅梅': 85, '小刚': 80, '小华': 75}

for i in classmates:
    print('Hello,', classmates[i])
