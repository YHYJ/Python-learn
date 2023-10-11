#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""只需要import pdb，然后在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点"""

import pdb

s = '0'
n = int(s)
pdb.set_trace()     # 断点，运行到此自动暂停
print(10 / n)
'''运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境
可以用命令p查看变量，或者用命令c继续运行'''