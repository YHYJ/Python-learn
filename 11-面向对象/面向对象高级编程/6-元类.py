#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass

metaclass —— 元类，简单的解释就是：
    创建实例前必须先创建类，所以：先创建类，然后创建实例
    创建类前必须先定义metaclass，所以：先定义metaclass，然后创建类
    连起来就是：先定义metaclass，就可以创建类，最后创建实例
所以，只有定义了metaclass才允许创建或者修改类
metaclass是Py面向对象里最难理解，也是最难使用的魔术代码
"""


# 先定义ListMetaclass，按习惯，元类的类名总是以Metaclass结尾，以便清楚地表示这是一个元类：
class ListMetaclass(type):
    """meatclass是类的模板，所以必须从‘type’类派生"""
    """一个简单的例子，元类Listmetaclass可以给自定义的MyList类增加一个add方法"""

    def __new__(cls, name, bases, attrs):
        """
        cls: 准备创建的类对象
        name：类的名字
        bases：类继承的父类的集合
        attrs：类的方法集合
        """
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 再定义MyList类，定义时指示使用元类ListMetaclass来定制类，传入关键字metaclass
class MyList(list, metaclass=ListMetaclass):
    pass


'''传入关键字metaclass时，魔术生效-
    -它指示Py解释器要通过ListMetaclass.__new__()来创建MyList
'''
L = MyList()    # 测试MyList是否可以调用add()方法
L.add(8)
L.add(12)
print(L)

'''直接在MyList定义中写上add()方法更简单
但总会遇到需要通过metaclass修改类定义的，ORM就是一个典型的例子 ——
    ORM全称“Object Relational Mapping”，即对象-关系映射-
    -就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表-
    -这样，写代码更简单，不用直接操作SQL语句
编写ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来
'''
