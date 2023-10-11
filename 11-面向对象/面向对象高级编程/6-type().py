#!/usr/bin/env python3

"""动态语言和静态语言最大的区别就是函数和类不是编译时定义的，而是运行时动态创建的"""


"""创建hello.py模块，定义一个Hello类
当Py解释器载入hello模块时，就会依次执行该模块的所有语句
执行结果动态创建出一个Hello的class对象"""
# 测试如下：
from hello import Hello
h = Hello()
h.hello()
print(type(Hello))  # Hello是一个类，它的类型就是type
print(type(h))      # h是一个实例，它的类型就是class Hello
'''type()函数可以查看一个类型或变量的类型'''


"""类的定义是运行时使用type()函数动态创建的
type()函数既可以返回一个对象的类型，又可以创建出新的类型"""
# 比如可以通过type()函数创建出Hello类，而无需通过class Hello():的定义：
# 1、先定义一个函数
# 2、再使用type()函数创建一个class对象　——
#     -指定类名Hi（hiya是hh这个实例的类型名）
#     -继承的父类
#     -class的方法名和函数绑定，这里将函数fn绑定到方法名hi
def fn(self, name="world"):     # 先定义函数
    print("Hi,%s." % name)

Hi = type('Hiya', (object,), dict(hi=fn)) # 创建Hello class
hh = Hi()
hh.hi()
print(type(Hi))
print(type(hh))
'''通过type()函数创建的类和直接写class是完全一样的-
    -因为Py解释器遇到class定义时，仅仅是扫描一下class定义的语法-
    -然后调用type()函数创建出class

正常情况下都用class Xxx():来定义类
但type()函数也允许动态创建出类来
也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同
要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现
本质上都是动态编译，会非常复杂'''
