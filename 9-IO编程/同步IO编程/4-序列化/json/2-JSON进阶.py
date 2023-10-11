#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""Py的dict对象可以直接序列化为JSON的{}
但更多时候用class表示对象然后序列化"""

import json

class Student():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Mccree', 50, 100)
#print(json.dumps(s))    # 抛出TypeError，因为Student对象不可序列化为JSON

"""查看dumps()方法的参数列表可以发现，除了第一个必须的obj参数外
dumps()方法还提供了一大堆的可选参数：
(https://docs.python.org/3/library/json.html#json.dumps)
这些可选参数用来定制JSON序列化
之所以无法把Student类实例序列化为JSON
是因为默认情况下dumps()方法不知道如何将Student实例变为一个JSON的{}对象
"""


"""可选参数default把任意一种对象变成一个可序列化为JSON的对象"""
# 只需为Student专门写一个转换函数，再把函数传进去即可：
def student2dict(std):
    return {
        'Hero_name': std.name,
        'Hero_age': std.age,
        'Hero_score': std.score
    }
print(json.dumps(s,default=student2dict))

# 下次如果遇到一个其他类的实例，照样无法序列化为JSON
# 下面方法可以把任意class的实例变为dict：
print(json.dumps(s,default=lambda obj: obj.__dict__))
'''因为通常class的实例都有一个__dict__属性，它是一个存储实例变量的dict
也有少数例外，比如定义了__slots__的class'''


"""可选参数object_hook把任意一个JSON的对象反序列化为一个类对象的实例"""
# loads()方法转换出一个dict对象，然后object_hook函数负责把dict转换为Teacher实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student))
'''打印出的是反序列化的一个Student的实例对象'''