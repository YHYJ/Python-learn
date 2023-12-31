#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""函数式编程

把函数作为参数传入，这样的函数称为高阶函数
函数式编程就是指这种高度抽象的编程范式
"""

"""面向过程的程序设计

函数是Python内建支持的一种封装，
把大段代码拆成函数，通过一层一层的函数调用-
-就可以把复杂任务分解成简单的任务，
这种分解称之为面向过程的程序设计
"""

"""函数是面向过程的程序设计的基本单元

函数式编程虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算
首先要明白计算机（Computer）和计算（Compute）的概念——
    在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令-
    -所以汇编语言是最贴近计算机的语言
    计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远-
    -对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言-
    -越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言
函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量——
    因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数没有副作用
允许使用变量的程序设计语言，由于函数内部的变量状态不确定——
    同样的输入，可能得到不同的输出，因此，这种函数是有副作用的

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数
Python对函数式编程提供部分支持
因为Py允许使用变量，Py不是纯函数式编程语言
"""