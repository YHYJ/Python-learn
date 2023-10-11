#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""列出当前目录下的所有文件和目录名
可以通过列表生成式以一行代码实现
"""

import os

file = [fi for fi in os.listdir('.')]   # os.listdir('.')列出当前目录结构
print(file)