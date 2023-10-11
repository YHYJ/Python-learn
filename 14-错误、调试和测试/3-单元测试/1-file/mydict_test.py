#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):      # 测试类，从unittest.TestCase继承

    def setUp(self):
        """在调用每个测试方法前执行，可定义具体操作"""
        print('setUp...')

    def tearDown(self):
        """在调用每个测试方法后执行，可定义具体操作"""
        print('tearDown...')

    def test_init(self):
        """测试方法以test开头，不以test开头的方法不是测试方法，测试时不执行"""
        d = Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

    def test_kayerror(self):
        """通过d['empty']访问不存在的key时,断言是否会抛出KeyError"""
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        """通过d.empty访问不存在的key时，期待抛出AttributeError"""
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()