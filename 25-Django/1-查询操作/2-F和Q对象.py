#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-11-04 20:01:12
Last modified: 2017-11-04 20:01:12
Python release: 3.6.2

"""
from django.db.models import F, Q


# F对象作用：比较两个属性
'''语法：
F('属性名')
'''


# Q对象作用：多个过滤器逐个调用表示逻辑与关系
'''语法：
Q(模型属性1__条件运算符=值) | Q(模型属性2__条件运算符=值)
'''

def bookList(request):
    '''bookInfos = [
        BookInfo.books.create('张小厨'),
        BookInfo.books.create('张小杰'),
    ]'''
    bookInfos = BookInfo.objects.all()

    """F和Q对象（F对象：比较两个属性     Q对象：多个过滤器逐个调用表示逻辑与关系）"""
    # F：
    # 1.查询阅读量大于评论量的书籍
    '''bookInfos = BookInfo.objects.filter(readcount__gt=F('commentcount'))'''
    # 2.查询阅读量大于2倍评论量的书籍(F对象支持运算)
    '''bookInfos = BookInfo.objects.filter(readcount__gt=F('commentcount')*2)'''
    # Q：
    # 1.查询阅读量大于20，并且编号小于3的图书
    '''bookInfos = BookInfo.objects.filter(readcount__gt=20, id__lt=3)'''
    '''bookInfos = BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)'''
    # 2.查询阅读量大于20，或编号小于3的图书
    '''bookInfos = BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))'''
    # 3.查询编号不等于3的书籍(Q对象前可以使用~操作符，表示非not)
    '''bookInfos = BookInfo.objects.filter(~Q(id=3))'''

    context = {'booklist': bookInfos}

    return render(request, 'Book/booklist.html', context)

