#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""计算BMI
要求：用户输入个人身高(m)、体重(kg)数据，根据BMI公式（体重/(身高)^2）计算用户的BMI指数，
并根据指数给出用户的身材
*   <18.5       过轻
*   18.5-25     正常
*   25-28       过重
*   28-32       肥胖
*   >32         严重肥胖
"""

# ?尝试创建一个类来解决
h = float(input('请输入你的身高(m)；'))
w = float(input('请输入你的体重(kg)：'))
bmi = w / (h * h)
print('你的BMI指数是：%.1f' % bmi)
if bmi < 18.5:
    print('你的体重过轻，注意补充营养哦！！！')
elif bmi >= 18.5 and bmi < 25:
    print('你的身材很好！！！')
elif bmi >= 25 and bmi < 28:
    print('你有一丢丢重喽，运动起来吧！！！')
elif bmi >= 28 and bmi < 32:
    print('pigff！！！')
else:
    print('可能是肿了！！！')
