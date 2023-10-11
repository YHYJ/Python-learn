#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文本系统的控制符：
\r：将光标移动到当前行的首位而不换行
\n：将光标移动到下一行而不移动到首位
\r\n：将光标移动到下一行首位
"""

import sys
from time import sleep


def viewBar(i):
    """
    进度条效果
    """
    output = sys.stdout
    for count in range(0,i + 1):
        second = 0.1
        sleep(second)
        output.write('\r进度:%.0f%%' % count)
    output.flush()
viewBar(100)
