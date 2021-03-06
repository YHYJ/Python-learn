#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""ORM全称“Object Relational Mapping”，即对象-关系映射
就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表"""

"""编写底层模块的第一步是先把调用接口写出来
比如使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User"""
# 应该写出这样的代码：
#class User(Model):
#    """定义类的属性到列的映射"""
#    id = IntegerField('id')
#    name = StringField('username')
#    email = StringField('email')
#    password = StringField('password')

# 创建一个实例
#u = User(id=12345,name='Michael',email='YJ1516268@outlook.com',password='YJmi1516268521')
# 保存到数据库
#u.save()
'''其中父类Model和属性类型StringField、IntegerField是由ORM框架提供的
剩下的魔术方法比如save()全部由metaclass自动完成
虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单'''

"""接下来按上面的接口实现该ORM"""
# 首先定义Field类：
class Field():
    """保存数据库表的字段名和字段类型"""
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__,self.name)

# 在Field的基础上，进一步定义各种类型的Field：
class StringField(Field):

    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):

    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')

# 定义最复杂的ModelMetaclass：
class ModelMetaclass(type):

    def __new__(cls, name, bases,attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping: %s ==> %s' % (k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings    # 保存属性和列的映射关系
        attrs['__table__'] = name           # 假设表名和类名一致
        return type.__new__(cls,name,bases,attrs)

# 定义基类Model
class Model(dict,metaclass=ModelMetaclass):

    def __init__(self,**kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql = "insert into %s (%s) values (%s)" % (self.__table__,','.join(fields),','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    """定义类的属性到列的映射"""
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345,name='Michael',email='YJ1516268@outlook.com',password='YJmi1516268521')
u.save()
'''save()方法打印出了可执行的SQL语句以及参数列表
只需要真正连接到数据库，执行该SQL语句，就可以完成真正的功能
'''













