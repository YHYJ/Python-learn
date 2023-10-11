#!/usr/bin/env python3

'''任何事物都有一个从创建，被使用，再到消亡的过程
在面向对象编程模型中，对象也有相似的命运：创建、初始化、使用、垃圾回收
不同的阶段由不同的方法负责执行'''

'''定义一个类时，用得最多的就是 __init__ 方法，而 __new__ 和 __call__ 使用得比较少'''


# __init__方法
'''__init__方法负责对象的初始化，系统执行该方法前，其实该对象已经存在了'''
class A:
    def __init__(self):
        print("__init__ ")
        super(A, self).__init__()

    def __new__(cls):
        print("__new__ ")
        return super(A, cls).__new__(cls)

    def __call__(self):  # 可以定义任意参数
        print('__call__ ')

A()
# 输出结果：
__new__
__init__
'''从输出结果来看， __new__方法先被调用，返回一个实例对象
接着 __init__ 被调用， __call__方法并没有被调用'''


# 改写成：
class A:
    def __init__(self):
        print("__init__ ")
        print(self)
        super(A, self).__init__()

    def __new__(cls):
        print("__new__ ")
        self = super(A, cls).__new__(cls)
        print(self)
        return self
    def __call__(self):  # 可以定义任意参数
        print('__call__ ')

# 输出结果：
__new__ 
<__main__.A object at 0x1007a95f8>
__init__ 
<__main__.A object at 0x1007a95f8>
'''从输出结果来看，__new__ 方法的返回值就是类的实例对象
这个实例对象会传递给 __init__ 方法中定义的 self 参数，以便实例对象可以被正确地初始化
如果 __new__ 方法不返回值（或者说返回 None）那么 __init__ 将不会得到调用，调用 init 也没什么意义
此外，Python 还规定 __init__ 只能返回 None 值，否则报错'''


# __init__方法可以用来做一些初始化工作，比如给实例对象的状态进行初始化：
def __init__(self, a, b):
    self.a = a
    self.b = b
    super(A, self).__init__()
# 另外，__init__方法中除了self之外定义的参数，都将与__new__方法中除cls参数之外的参数是必须保持一致或者等效
class B:
    def __init__(self, *args, **kwargs):
        print("init", args, kwargs)

    def __new__(cls, *args, **kwargs):
        print("new", args, kwargs)
        return super().__new__(cls)

B(1, 2, 3)
# 输出结果：
new (1, 2, 3) {}
init (1, 2, 3) {}


# __new__ 方法
'''一般不会去重写该方法，它作为构造函数用于创建对象，是一个工厂函数，专用于生产实例对象
著名的设计模式之一：单例模式，就可以通过此方法来实现
在自己写框架级的代码时可能会用到它，也可以从开源代码中找到它的应用场景，例如微型 Web 框架 Bootle 就用到了'''
class BaseController(object):
    _singleton = None
    def __new__(cls, *a, **k):
        if not cls._singleton:
            cls._singleton = object.__new__(cls, *a, **k)
        return cls._singleton
'''这段代码出自 https://github.com/bottlepy/bottle/blob/release-0.6/bottle.py'''
'''这就是通过 __new__ 方法实现单例模式的一种方式：
如果实例对象存在了就直接返回该实例即可，如果没有，那么就先创建一个实例，再返回
当然，实现单例模式的方法不只一种，Python之禅有说：
There should be one-- and preferably only one --obvious way to do it.
用一种方法，最好是只有一种方法来做一件事'''


# __call__ 方法
'''关于 __call__ 方法，不得不先提到一个概念，就是可调用对象（callable）
平时自定义的函数、内置函数和类都属于可调用对象，但凡是可以把一对括号()应用到某个对象身上都可称之为可调用对象
判断对象是否为可调用对象可以用函数 callable
如果在类中实现了 __call__ 方法，那么实例对象也将成为一个可调用对象'''
# 回到最开始的那个例子：
a = A()
print(callable(a))  # True
'''a是实例对象，同时还是可调用对象，那么就可以像函数一样调用它
a()  # __call__'''
'''实例对象也可以像函数一样作为可调用对象来用，那么，这个特点在什么场景用得上呢？
这个要结合类的特性来说，类可以记录数据（属性），而函数不行（闭包某种意义上也可行），利用这种特性可以实现基于类的装饰器，在类里面记录状态'''
# 比如，下面这个例子用于记录函数被调用的次数：
class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@Counter
def foo():
    pass

for i in range(10):
    foo()

print(foo.count)  # 10
'''在 Bottle 中也有 call 方法 的使用案例
另外，stackoverflow 也有一些关于 call 的实践例子
如果项目中需要更加抽象化、框架代码，那么这些高级特性往往能发挥出它作用'''
