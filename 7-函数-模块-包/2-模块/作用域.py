#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = '1516 YJ'

"""
一个模块中可能会定义很多函数和变量-
-有的函数和变量希望给别人使用,有的函数和变量希望仅仅在模块内部使用-
    -在Py中通过_和__前缀实现
"""

# 类似abc,xy的函数或变量是公开的（public）,可以被直接引用 ——
'''比如:abc,x123,PI等'''
    
# 类似__xxx__的变量是特殊变量,可以被直接引用,但是有特殊用途 ——
'''上面的__author__和__name__就是特殊变量-
    -hello模块定义的文档注释也可以用特殊变量__doc__访问-
    -自己的变量一般不要用这种变量名
'''

# 类似_xxx和__xxx的函数或变量是非公开的（private）,不应该被直接引用 ——
'''比如_abc，__abc等
之所以说非公开函数和变量“不应该”被直接引用,而不是“不能”被直接引用 —— 
    因为Py并没有一种方法可以完全限制访问非公开函数或变量
    但是,从编程习惯上不应该引用非公开函数或变量
'''


"""非公开函数或变量不应该被别人引用，那它们有什么用"""
# 例子：
def _private_1(name):
    return 'Hello,%s' % name

def _private_2(name):
    return 'Hi,%s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
h = greeting('YJ')
print(h)
'''greeting()是公开函数，但内部逻辑用非公开函数隐藏起来了
这样，调用greeting()函数不用关心内部的非公开函数细节
这是一种非常有用的代码封装和抽象的方法'''
# 即：外部不需要引用的函数全部定义成非公开(private)，只有外部需要引用的函数才定义为公开(public)