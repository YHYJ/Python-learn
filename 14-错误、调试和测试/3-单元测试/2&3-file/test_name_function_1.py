#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest     # 为函数编写测试用例，要先导入模块unittest以及要测试的函数
from name_function_1 import get_formatted_name

# 创建用于包含一系列针对get_formatted_name()的单元测试。类名最好与要测的函数相关，并包含字样Test
class TestNames(unittest.TestCase):   # 要继承unittest.TestCase
    """测试name_function_1.py的函数get_formatted_name()"""

    def test_first_last_name(self):     #运行测试用例时所有以test_打头的方法将自动调用
        """测试能否正确的处理像Janis Joplin这样的姓名"""
        formatted_name = get_formatted_name('yj','1516')  #调用要测试的函数，存储要测试的返回值
        #使用unittest类最有用的功能之一，一个 ‘断言方法’ —— assertEqual()
        self.assertEqual(formatted_name,'Yj 1516')  #并向它传递返回值formatted_name和期望值

if __name__ == '__main__':
    unittest.main()     #运行测试