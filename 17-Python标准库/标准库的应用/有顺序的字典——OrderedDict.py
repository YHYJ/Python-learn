#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用模块collections中的OrderedDict类创建字典并记录其中的键—值对的添加顺序.

OrderedDict实例的行为几乎与字典相同，区别只在于记录了键—值对的添加顺序.
"""

from collections import OrderedDict

#调用OrderedDict()来创建一个空的有序字典,并将其存储在favorite_languages中
favorite_languages = OrderedDict()  #创建一个OrderedDict类的实例

favorite_languages['张三'] = 'python'     #存储的键-值对的顺序
favorite_languages['李四'] = 'c'
favorite_languages['王二麻子'] = 'ruby'
favorite_languages['赵二傻子'] = 'python'

for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is" +
          language.title() + ".")