#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""把print()替换为logging是第3种方式"""
# logging不会抛出错误，而且可以输出到文件：
import logging
logging.basicConfig(filename='logging.log', level=logging.INFO)

s = '0'
n = int(s)
logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')
print(10 / n)
'''logging允许指定记录信息的级别，level=logging. ——
    DEBUG     详细信息，调试问题时使用
    INFO 	  证明事情按预期工作
    WARNING	  表明发生了一些意外，或者不久的将来会发生问题（如‘磁盘满了’）但代码正常运行
    ERROR	  由于更严重的问题，代码已不能执行一些功能
    CRITICAL  严重错误，表明代码已不能继续运行
等几个级别.
当指定level=INFO时，logging.debug不起作用
同理指定level=WARNING后，debug和info不起作用
这样可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息
logging通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件
'''
