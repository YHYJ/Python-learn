#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""不能处理中间名"""

def get_formatted_name(firstname,lastname):
    """输出整洁的名字"""
    full_name = firstname + ' ' + lastname
    return full_name.title()