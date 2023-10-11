#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""在Python中，一个.py文件就称之为一个模块（Module）

例如：一个abc.py文件就是一个abc模块,一个xyz.py文件就是一个xyz模块
在程序开发过程中,随着代码的增加,一个文件里代码会越来越长,越来越不容易维护
为了编写可维护的代码,开发者把很多函数分组,分别放到不同的文件里形成模块-
-这样每个文件包含的代码就相对较少,很多编程语言都采用这种组织代码的方式
"""

"""自己创建模块时要注意命名,不能和Python自带的模块名称冲突
例如系统自带了sys模块，自己的模块就不可命名为sys.py-
-否则无法导入系统自带的sys模块
"""

"""使用模块的好处 —— 
    1、最大的好处是大大提高了代码的可维护性
    2、编写代码不必从零开始 —— 当一个模块编写完毕，就可以被引用
    3、使用模块可以避免函数名和变量名冲突-
       -相同名字的函数和变量完全可以分别存在不同的模块中
       -因此,在编写模块时,不必考虑名字会与其他模块冲突
       -但是也尽量不要与内置函数名字冲突
"""

"""Python内置函数(Built-in Functions)
abs()   all()   any()   ascii()
bin()   bool()  bytearray()    bytes()
callable()    chr()    classmethod()    compile()   complex()
delattr()     dict()   dir()    divmod()
enumerate()   eval()   exec()   filter()    float()    format()    frozenset()
getattr()     globals()
hasattr()     hash()    help()  hex()
id()    input()    int(0    isinstance()    issubclass()    iter()
len()   list()     locals()
map()   max()      memoryview()    min()
next()
object()    oct()   open()    ord()
pow()    print()    property()
range()    repr()    reversed()    round()
set()    setattr()    slice()    sorted()    staticmethod()    str()    sum()    super()
tuple()    type()
vars()
zip()
__import__()
"""