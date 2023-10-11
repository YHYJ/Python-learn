#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-11-04 20:26:31
Last modified: 2017-11-04 20:26:31
Python release: 3.6.2

聚合函数：使用aggregate()过滤器调用聚合函数，返回单个对象（聚合函数包括：Avg，Max，Min，Sum，Count
使用Count时，一般不需要 aggregate()过滤器，直接调用即可
"""
from django.db.models import Sum


def bookList(request):
    '''bookInfos = [
        BookInfo.books.create('张小厨'),
        BookInfo.books.create('张小杰'),
    ]'''
    bookInfos = BookInfo.objects.all()

    """聚合函数：使用aggregate()过滤器调用聚合函数，返回单个对象（聚合函数包括：Avg，Max，Min，Sum，Count）"""
    # 统计总共阅读量
    readcount = BookInfo.objects.aggregate(Sum('readcount'))

    context = {
        'booklist': bookInfos,
        'readcount': readcount,
    }

    return render(request, 'Book/booklist.html', context)
