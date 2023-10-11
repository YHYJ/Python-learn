#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""能处理包含或不包含中间名的名字"""

def get_formatted_name(firstname,lastname,middlename=''):   #将某个参数设置为可选的可在函数定义中将该参数移到形参列表末尾，并将默认值指定为一个空字符串
    """生成整洁的姓名"""
    #还要添加一个if测试，以便根据是否提供了中间名相应地创建姓名
    if middlename:
        full_name = firstname + ' ' + middlename + ' ' + lastname
    else:
        full_name = firstname + ' ' + lastname
    return full_name.title()