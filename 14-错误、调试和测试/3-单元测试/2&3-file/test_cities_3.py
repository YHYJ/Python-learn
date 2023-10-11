#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from city_functions_3 import city_function

class TestCityCountry(unittest.TestCase):
    """测试one_three_city_functions.py里的函数city_function()"""

    def test_city_contury(self):
        """能否正确返回city,country格式的字符串"""
        cc = city_function(city='santiago',country='chile')
        self.assertEqual(cc,'Santiago,Chile')

    def test_city_country_population(self):
        """能否正确返回city,country - population xxx格式的字符串"""
        cc = city_function(
            city='santiago',country='chile',population='5000000')
        self.assertEqual(cc,'Santiago,Chile - Population 5000000')

if __name__ == '__main__':
    unittest.main()