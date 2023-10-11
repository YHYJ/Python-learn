#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from name_function_2 import get_formatted_name

class TestNames(unittest.TestCase):
    """测试name_function_two.py的函数get_formatted_name()"""

    def test_first_last_name(self):
        """能否正确处理像Yj 1516这样的姓名"""
        formatted_name = get_formatted_name('yj','1516')
        self.assertEqual(formatted_name,'Yj 1516')

    def test_first_last_middle_name(self):
        """能否正确处理像Yj Linux 1516这样的姓名"""
        formatted_name = get_formatted_name(
            firstname='yj',lastname='1516',middlename='linux')
        self.assertEqual(formatted_name,'Yj Linux 1516')

if __name__ == '__main__':
    unittest.main()