#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from work_5 import Employee

class TestEmployee(unittest.TestCase):
    """测试two_four_work.py的类 Employee()"""

    def test_give_default_raise(self):
        """测试默认年薪"""
        employee = Employee('安','娜',100000)     # 要测试Employee类，先创建一个它的实例
        annual = employee.give_raise()           # 测试Employee类的give_raise()方法，使用默认值，将结果保存到变量annual
        self.assertEqual(annual,'安 娜原来年薪是100000，现在是105000')

    def test_give_custom_raise(self):
        """测试指定年薪"""
        employee = Employee('安','娜',100000)
        annual = employee.give_raise(salary_add=8000)
        self.assertEqual(annual,'安 娜原来年薪是100000，现在是108000')

if __name__ == '__main__':
    unittest.main()