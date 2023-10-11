#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Py内置了一套try...except...finally...的错误处理机制"""

try:        # 程序在try内部执行某行代码引发异常时直接跳过try中剩下的代码
    print('try...')
    r = 10 / 2
    print('result:', r)
except ValueError as error:     # except捕获Error
    print('无效字符:', error)
except ZeroDivisionError as error:
    print('0不能做除数:', error)
else:                           # try成功运行自动执行else语句
    print('no error'.title())
finally:                        # 一定执行finally语句，但可以没有finally语句
    print('end'.upper())
'''当认为某些代码可能会出错时，就可以用try来运行这段代码
如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块
执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕'''


"""try...except捕获错误可以跨越多层调用
比如函数main()调用bar()，bar()调用foo()，结果foo()出错了"""
# 只要main()捕获到了错误，就可以处理：


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as error:  # except捕获Error，但不能捕获异常信息，Exception能
        print('Error:', error)
    finally:
        print('end'.upper())


main()
'''也就是说只要在合适的层次捕获错误就可以了。这样就大大减少了写try...except...finally的麻烦'''


'''Py内置的try...except...finally用来处理错误十分方便
出错时会分析错误信息并定位错误发生的代码位置是最关键的
程序也可以主动抛出错误，让调用者来处理相应的错误
但应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因'''


print("*"*25 + "处理 FileNotFoundError 异常" + "*"*25)
# 使用文件时，一种常见的问题是找不到文件：
# 读取文件alice.txt，但one_two_alice.py所在的目录中没有这个文件 ——> one_two_alice.py


print("*"*25 + "使用多个文件" + "*"*25)
# 多分析几本书，将这个程序的大部分代码移到一个名为count_words()的函数中
# 这样对多本书进行分析时将更容易 ——> one_three_word_count.py


print("*"*25 + "出现异常时不反馈异常信息" + "*"*25)
# 并非每次捕获到异常时都需要告诉用户，有时候希望程序在发生异常时继续运行而不提示
# 可在except代码块中使用pass让Py什么都不做 ——> one_three_word_count.py
