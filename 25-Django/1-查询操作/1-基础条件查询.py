#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-11-04 19:57:34
Last modified: 2017-11-04 19:57:34
Python release: 3.6.2
查询语句是属性名称和比较运算符间使用两个下划线相连，所以定义的模型属性名不能包括多个下划线
实现sql中where的功能，可以调用过滤器filter()、exclude()、get()
"""
from django.shortcuts import render
from .models import BookInfo


def bookList(request):
    '''bookInfos = [
        BookInfo.books.create('张小厨'),
        BookInfo.books.create('张小杰'),
    ]'''
    bookInfos = BookInfo.objects.all()
    # 限制查询集 ——获取书籍信息第1、2项
    '''bookInfos = BookInfo.books.all()[0:2]'''
    # 1.查询id为1的书籍(exact : 判断相等（iexact：不区分大小写）)
    '''bookInfos = BookInfo.objects.filter(id__exact=1)'''
    # 2.查询书名包含‘湖’的书籍(contains : 是否包含（icontains：不区分大小写）)
    '''bookInfos = BookInfo.objects.filter(name__contains='湖')'''
    # 3.查询书名以‘部’结尾的书籍(startswith/endswith : 以什么开头／以什么结尾（istartswith & iendswith：不区分大小写）)
    '''bookInfos = BookInfo.objects.filter(name__endswith='部')'''
    # 4.查询书名不为空的书籍(isnull : 是否为null)
    '''bookInfos = BookInfo.objects.filter(name__isnull=False)'''
    # 5.查询编号为2或4的书籍(pk:主键/id) (in : 是否包含在范围内)
    '''bookInfos = BookInfo.objects.filter(pk__in=[2,4])'''
    # 6.查询编号大于2的书籍(gt：>    gte：>=   lt：<    lte：<=)
    '''bookInfos = BookInfo.objects.filter(pk__gt=2)'''
    # 7.查询id不等于3的书籍(exclude : 条件以外的数据)
    '''bookInfos = BookInfo.objects.exclude(id=3)'''
    # 8.查询1980年发表的书籍(year、month、day、week_day、hour、minute、second)
    '''bookInfos = BookInfo.objects.filter(pub_date__year=1980)'''
    # 9.查询1990年1月1日后发表的书籍
    '''from datetime import date
    bookInfos = BookInfo.objects.filter(pub_date__gt=date(1990, 1, 1))'''

    context = {'booklist': bookInfos}

    return render(request, 'Book/booklist.html', context)

