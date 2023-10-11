#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""with 语句适用于对资源进行访问的场合.

确保不管使用过程中是否发生异常都会执行必要的“清理”操作,释放资源.
比如文件使用后自动关闭、线程中锁的自动获取和释放等
"""


'''要使用 with 语句，首先要明白上下文管理器这一概念.
有了上下文管理器，with 语句才能工作.'''

'''
#上下文管理协议：包含方法【__enter__()和__exit__()】，支持该协议的对象要实现这两个方法

#上下文管理器：支持【上下文管理协议】的对象，这种对象实现了__enter__()和__exit__()方法
             【上下文管理器】定义执行with语句时要建立的【运行时上下文】，负责执行with语句块
             上下文中的进入与退出操作
             通常使用with语句调用上下文管理器，也可以以直接调用其方法来使用

#运行时上下文：由【上下文管理器】创建，通过上下文管理器的__enter__()和__exit__()方法实现。
             __enter__()方法在语句体执行之前进入运行时上下文，__exit__()在语句体执行
             完后从运行时上下文退出。with语句支持运行时上下文这一概念。

#上下文表达式：with语句中跟在关键字with后的表达式，该表达式返回一个【上下文管理器】对象。

#语句体：with语句包裹起来的代码块，在执行语句体之前会调用__enter__()方法，执行完语句体之后会执行__exit__()方法。
'''


# with 语句的语法格式：
'''
# with '上下文表达式' as '目标':  #'上下文表达式'返回一个上下文管理器对象但并不赋给'目标'
    '语句体'   #如果指定了as子句,会将上下文管理器的__enter__()方法的返回值赋给'目标'
#'目标'可以是单个变量,或者由()括起来的元组(不能是仅仅由','分隔的变量列表,必须加'()')
'''


#使用 with 语句操作文件对象：      #已经加入对上下文管理协议支持的还有模块 threading、decimal 等
with open(r'/home/yj/Documents/code/Py/3.5/9--文件操作/data/withfile.txt') as file:
    for line in file:
        print(line)
#这里使用了with语句，不管处理文件过程中是否发生异常，都能保证with语句执行完后关闭打开的文件句柄

print('*'*100)

#使用传统try/finally方式：
somefile = open(r'/home/yj/Documents/code/Py/3.5/9--文件操作/data/withfile.txt')
try:
    for line in somefile:
        print(line)
finally:
    somefile.close()    #代码量多且要手动关闭文件句柄


# with 语句执行过程：
'''【context_manager】——上下文管理器 ； 【context_expression】——上下文表达式
context_manager = context_expression
exit = type(context_manager).__exit__
value = type(context_manager).__enter__(context_manager)
exc = True   # True 表示正常执行，即便有异常也忽略；False 表示重新抛出异常，需要对异常进行处理
try:
    try:
        target = value  # 如果使用了 as 子句
        with-body     # 执行 with-body
    except:
        # 执行过程中有异常发生
        exc = False
        # 如果 __exit__ 返回 True，则异常被忽略；如果返回 False，则重新抛出异常
        # 由外层代码对异常进行处理
        if not exit(context_manager, *sys.exc_info()):
            raise
finally:
    # 正常退出，或者通过 statement-body 中的 break/continue/return 语句退出
    # 或者忽略异常退出
    if exc:
        exit(context_manager, None, None, None)
    # 缺省返回 None，None 在布尔上下文中看做是 False

1、执行上下文表达式context_expression，生成上下文管理器context_manager。
2、调用上下文管理器的__enter__()方法。如果使用了 as 子句，则将__enter__()方法
   的返回值赋给 as 子句中的target(s)。
3、执行语句体 with-body。
4、不管执行过程是否发生异常，执行__exit__()方法来执行’清理‘工作如释放资源等。
   如果执行过程中没有出现异常，或者语句体中执行了语句 break/continue/return，
   则以None作为参数调用__exit__(None,None,None)；如果出现异常，则使用sys.exc_info
   得到的异常信息为参数调用__exit__(exc_type,exc_value,exc_traceback)。
5、出现异常时，如果__exit__(type,value,traceback)返回False，则会重新抛出异常，
   让 with 之外的语句逻辑来处理异常，这是通用做法。如果返回True，则忽略异常不再进行处理。
'''