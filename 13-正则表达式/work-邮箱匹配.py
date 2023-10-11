#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""写一个验证Email地址的正则表达式
版本一应该可以验证出类似的Email：
someone@gmail.com
bill.gates@microsoft.com

版本二可以验证并提取出带名字的Email地址：
<Tom Paris> tom@voyager.org
"""

import re

# 版本一：
email = input('请输入邮箱：')
if re.match(r'^([A-Za-z0-9]+)(@)([a-z0-9A-Z]+)(.)([a-zA-Z]+)$', email):
    print(email.lower())
else:
    print('非法邮箱！！')


# 版本二：

email = input('请输入署名邮箱:')
reemail = re.compile(
    (r'^[<|{]([a-z\sA-Z]+)[}|>]\s([a-zA-Z.0-9_]+)'
     '(@)([0-9a-zA-Z]+)(.)([a-zA-Z]+)$')
)
if reemail.match(email):
    print(reemail.match(email).groups())
    print('邮箱所有者：', reemail.match(email).group(1).title())
    print(reemail.match(email).group(2)
          + reemail.match(email).group(3)
          + reemail.match(email).group(4)
          + reemail.match(email).group(5)
          + reemail.match(email).group(6))
else:
    print('非法邮箱！！')
