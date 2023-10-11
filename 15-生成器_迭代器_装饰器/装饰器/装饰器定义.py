#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""装饰器（decorator）在代码运行期间动态增加功能

是放在函数定义前面的指令
Py在函数运行前根据装饰器来增加函数的功能
本质上，装饰器就是一个返回值是函数的高阶函数
"""
import time
#from random import randint

#@randint
#def topics():
#    pass
'''在topics函数前面加上 @randint
让Py在运行topics()的代码前先运行randint()的代码'''


"""因为函数也是一个对象，而且函数对象可以被赋值给变量，所以通过变量也能调用该函数"""
# 比如：
def now():
    print('2017-6-7')
f = now
f()


"""函数对象有一个__name__属性"""
# __name__属性可以拿到函数的名字：
print('函数now()的名字：',now.__name__ + '\n' + '变量f指向的对象的名字：',f.__name__)


"""增强now()函数的功能（另定义一个time()函数）
比如，在函数调用前后自动打印日志，但又不希望修改now()函数"""
# 使用装饰器：
def log(func):
    """装饰器，接受一个函数作为参数，并返回一个函数参数"""
    def wrapper(*args, **kwargs):                    # 1
        print('func name：%s()' % func.__name__)     # 打印日志
        #  return func(*args,**kwargs)               # 2
        func(*args,**kwargs)                         # 2
    return wrapper


@log            # 相当于执行了语句：my = log(mytime)
def mytime():
   print(time.ctime())
    # return 1
# my = log(mytime)
mytime()          # 调用time()函数，会在运行time()函数前运行log()函数打印一行日志
'''由于log()是一个装饰器，返回一个函数，所以原来的mytime函数仍然存在
只是现在mytime变量指向了新的函数wrapper
于是调用mytime()将执行wrapper()函数

1处 —— wrapper()函数的参数定义是(*args, **kw)-
      -因此wrapper()函数可以接受任意参数的调用-
      -这里是接受函数mytime的调用
在wrapper()函数内，首先打印日志，紧接着 ——
2处 —— 调用原来的time()函数，如果被装饰函数有返回值的话此处需要使用return，否则返回None
'''


"""如果装饰器本身需要传入参数，那就需要编写一个返回装饰器的高阶函数
即在装饰器外层加一个def定义用来接收装饰器的参数，然后在装饰器里的函数里使用这个参数"""
# 比如，要自定义log的文本：
def logs(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s：%s()' % (text, func.__name__))
            func(*args,**kwargs)
        return wrapper
    return decorator

@logs('函数名')        # 相当于执行了语句：now_date_time = logs('函数名')(now_date_time)
def now_date_time():
    print('2017-6-7 15:58')
now_date_time()
'''首先执行log('execute')，返回的是decorator()函数-
   -再调用返回的函数，参数是now_date_time函数，返回值最终是wrapper函数
'''

# 经过装饰器装饰之后，函数的__name__已经从原来的名字变成了'wrapper'
print(now_date_time.__name__)
'''因为返回的wrapper()函数名字就是'wrapper'
所以，需要把原始函数的__name__等属性复制到wrapper()函数中
否则，有些依赖函数签名的代码执行就会出错
'''


# 不需要编写wrapper.__name__ = func.__name__这样的代码
# Python内置的functools.wraps效力于此
# 所以，一个完整的decorator的写法如下：
# >> ./定义一个完整的装饰器.py


"""在面向对象（OOP）的设计模式中，装饰器被称为装饰模式
   面向对象的装饰模式需要通过继承和组合来实现
   而Py除了支持面向对象的装饰模式外
   直接从语法层次支持装饰器
   Python的装饰器可以用函数实现，也可以用类实现
"""
