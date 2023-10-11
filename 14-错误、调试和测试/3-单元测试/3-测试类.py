#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("*"*25 + "各种断言方法" + "*"*25)
# unittest.TestCase 类中提供了很多断言方法
# 断言方法检查指定应该满足的条件是否确实满足
# 如果该条件确实满足，对程序行为的假设就得到了确认，可以确信其中没有错误
# 如果指定应该满足的条件并不满足，Py将引发异常
'''
   7个常用的断言方法，只有在继承了 unittest.TestCase 的类中才能使用这些方法
______________________________________________________________________
             方法                              用途
----------------------------------------------------------------------
        assertEqual(a,b)                核实返回值a == b
        assertNotEqual(a,b)             核实返回值a != b
        assertTrue(x)                   核实返回值x为True
        assertFalse(x)                  核实返回值x为False
        assertIn(item,list)             核实返回值item在列表list中
        assertNotIn(item,list)          核实返回值item不在列表list中
        assertRaises(KeyError)          核实抛出指定类型的异常，与with搭配
'''


print("*"*25 + "一个管理匿名调查的类AnonymousSurvey()" + "*"*25)
"""类的测试与函数的测试相似，大部分都是测试类中的方法，但存在一些不同之处"""
# 编写一个帮助管理匿名调查的类进行测试 ——> survey_4.py ——> AnonymousSurvey()
"""AnonymousSurvey类可用于进行简单的匿名调查，现在进行改进：
    让每位用户都可输入多个答案
    编写一个方法，它只列出不同的答案，并指出每个答案出现了多少次
    在survey_4.py中再编写一个类，用于管理非匿名调查
上述修改可能会影响AnonymousSurvey类的当前行为
编写针对这个类的测试以确认在开发这个模块时没有破坏既有行为
"""

print("*"*25 + "测试AnonymousSurvey()类" + "*"*25)
"""编写一个单元测试，对AnonymousSurvey类的行为的一个方面进行验证：
    如果用户面对调查问题时提供了1个或者多个答案，答案是否被妥善地存储
    在存储答案后，使用方法assertIn()来核实它包含在答案列表中
"""
# ——> test_survey_4.py
"""将创建一个调查对象和一组答案的代码写到 setUp() 方法，避免重复
方法test_single_store_response()和test_three_store_responses()将使用
setUp() 方法里定义的对象和答案来提高测试的效率
"""

print("*"*25 + "测试类时设置方法 setUp() 的便利性" + "*"*25)
"""方法 setUp() 让测试方法编写更容易：
    可在setUp()方法中创建一系列实例并设置它们的属性
    相比于在每个测试方法中都创建实例并设置其属性，这要容易得多
"""


print("*"*25 + "work" + "*"*25)
#定义一个显示雇员姓名年薪资料的类 ——> work_5.py
#测试这个类 ——> test_work_5.py
#以setUp()改写这个测试实例 ——> test_setup_work_5.py