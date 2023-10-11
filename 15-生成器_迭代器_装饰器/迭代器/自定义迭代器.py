#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-23 14:38:05
Last modified: 2017-09-23 14:38:05
Python release: 3.6.2

自定义迭代器，即实现了__iter__和__next__方法的对象
"""


class MyList(object):
    """自定义可迭代对象"""
    def __init__(self):
        self.items = list()

    def add(self, element):
        self.items.append(element)

    def __iter__(self):
        myiterator = MyIterator(self)
        return myiterator


class MyIterator(object):
    """自定义可迭代对象MyList的迭代器"""
    def __init__(self, mylist):
        self.mylist = mylist
        self.current = 0    # 记录当前访问到的位置

    def __next__(self):
        if self.current < len(self.mylist.items):
            item = self.mylist.items[self.current]    # 返回当前访问到的位置的元素
            self.current += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == "__main__":
    mylist = MyList()
    myIterator = MyIterator(mylist)
    mylist.add(u) for u in [1,2,3,4,5,6])
    # mylist.add(2)
    # mylist.add(3)
    # mylist.add(4)
    # mylist.add(5)
    # mylist.add(6)
    print(mylist)
    print(myIterator)
    for i in mylist:
        print(i)
