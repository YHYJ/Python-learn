#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""可以自定义支持上下文管理协议的类
自定义的上下文管理器要实现上下文管理协议所需要的__enter__()和__exit__()两个方法
"""

#context_manager.__enter__()：
'''进入上下文管理器的运行时上下文，在语句体执行前调用.
with 语句将该方法的返回值赋给 as 子句的target（指定 as 子句的话）.'''

#context_manager.__exit__(exc_type,exc_value,exc_traceback)：
'''退出与上下文管理器相关的运行时上下文，返回一个布尔值表示是否对发生的异常进行处理.
参数表示引起退出操作的异常，如果退出时没有发生异常则3三个参数都为None。
如果发生异常，返回True表示不处理异常，否则会在退出该方法后重新抛出异常由with之外的代码进行处理。
如果该方法内部产生异常。则会取代由statement_body中语句产生的异常。
处理异常时，不能重新抛出通过参数传递进来的异常，只要将返回值设置为False即可。
之后，上下文管理代码会检测是否__exit__()失败来处理异常'''



"""构建上下文管理器——注意：上下文管理器必须同时提供__enter__()和__exit__()方法的定义"""

#1、自定义支持 with 语句的对象：
'''假设一个资源DummyResource，这种资源需要在访问前先分配，使用完后再释放.
分配操作可以写在__enter__()方法中，释放操作可以写在__exit__()方法中.'''
class DummyResource:
    def __init__(self, tag):
        self.tag = tag
        print('Resource [%s]' % tag)

    def __enter__(self):
        print('[Enter %s]:Allocate resource.' % self.tag)
        return self     # 可以返回不同的对象

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('[Exit %s]:Free resource.' % self.tag)
        if exc_tb is None:
            print('[Exit %s]:Exited without exception.' % self.tag)
        else:
            print('[Exit %s]:Exited with exception raised.' % self.tag)
            return False    #可以省略，缺省的None也被看作False
#__enter__()返回的是自身的引用，此引用可以赋给 as 子句中的target变量，返回值类型不必是上下文管理器本身
#__exit__()方法中对变量exc_tb进行检测，如不是None，表示发生异常，返回False表示需要外部代码逻辑处理异常。
#           如果没有发生异常，缺省返回值为None，在布尔环境也看作False，但因为没有异常发生，__exit__()
#           的3个参数都为None，上下文管理器代码可以检测这种情况，做正确处理。

#2、使用自定义的支持 with 语句的对象访问DummyResource
with DummyResource('Normal'):
    print('[with-body] Run without exceptions.')
#先执行完语句体 with-body ，再执行__exit__()方法释放资源

print('*'*100)
with DummyResource('with-Exception'):
    print('[with-body] Run with exception.')
    raise Exception     #raise显示的引发异常，一旦执行raise语句，raise后的代码不能执行
    print('[with-body] Run with exception.Failed to finish statement-body')
#with-body中发生异常时with-body并没有执行完，但资源会保证被释放掉。
#         同时产生的异常由with语句之外的代码逻辑来捕获处理。