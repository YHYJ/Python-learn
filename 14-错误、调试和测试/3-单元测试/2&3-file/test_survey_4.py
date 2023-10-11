#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""测试类"""

import unittest
from survey_4 import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):   # 对测试用例命名，并继承unittest.TestCase
    """针对AnonymousSurvey类的测试"""
    def setUp(self):
        """创建一个调查对象和一组答案，供需要的测试方法使用"""
        question = "你最喜欢的颜色是什么？"
        self.survey = AnonymousSurvey(question)          # 创建一个调查对象实例，包含前缀self
        self.responses = ['紫色','银灰','浅蓝','青色']     # 创建一个答案列表，包含前缀self

    def test_single_store_response(self):
        """测试单个答案是否被妥善保存在调查结果列表responses[]"""
        self.survey.store_response(self.responses[1])           # 使用类方法store_response()存储第1个答案
        self.assertIn(self.responses[1],self.survey.responses)  # 检查 '紫色' 是否包含在列表responses中

    def test_more_store_response(self):
        """测试多个答案是否被妥善保存在调查结果列表responses[]"""
        for response in self.responses:          # 对每个答案调用store_response()进行存储
            self.survey.store_response(response) # 存储答案，循环完毕则保存完毕
        for response in self.responses:          # 确认每个答案都包含在列表responses中
            self.assertIn(response,self.survey.responses)

if __name__ == '__main__':
    unittest.main()