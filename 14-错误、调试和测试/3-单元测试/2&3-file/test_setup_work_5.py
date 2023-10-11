#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from work_5 import Employee

class TestEmployee(unittest.TestCase):
    """测试two_four_work.py的类 Employee()"""

    def setUp(self):
        """创建一个雇员实例和其基本年薪信息，供需要的测试方法使用"""
        firstname = '安'
        lastname = '娜'
        salary = 100000
        self.employee = Employee(firstname,lastname,salary)

    def test_give_default_raise(self):
        """测试默认年薪"""
        annual = self.employee.give_raise()
        self.assertEqual(annual,'安 娜原来年薪是100000，现在是105000')

    def test_give_custom_raise(self):
        """测试指定年薪"""
        annual = self.employee.give_raise(salary_add=13000)
        self.assertEqual(annual,'安 娜原来年薪是100000，现在是113000')

if __name__ == '__main__':
    unittest.main()