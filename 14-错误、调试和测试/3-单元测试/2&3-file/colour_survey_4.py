#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""调查最喜欢的颜色并最终显示调查结果"""

from survey_4 import AnonymousSurvey

#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "你最喜欢的颜色是什么？"
survey = AnonymousSurvey(question)

#显示问题
survey.show_question()
print("输入‘q’回车退出.\n")

#存储答案
while True:
    response = input("请输入你的答案：")
    if response == 'q':     #退出机制
        break
    elif response == '':
        response = '(未填写)'
    survey.store_response(response)

#显示调查结果
print("\n感谢您参加本次调查！")
survey.show_results()