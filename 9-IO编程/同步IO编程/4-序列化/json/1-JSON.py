#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""
如果要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML
更好的方法是序列化为JSON —— 
    -因为JSON表示出来就是一个字符串，可以被所有语言读取
    -也可以方便地存储到磁盘或者通过网络传输
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便

模块内置的json模块提供了非常完善的Py对象到JSON格式的转换
JSON标准规定JSON编码是UTF-8，所以总能正确地在Py的str与JSON的字符串之间转换
"""


"""JSON表示的对象就是标准的JS语言的对象，JSON和Py内置的数据类型对应如下：
        JSON类型                 Py类型
------- {}                      dict
------- []                      list
------- "string"                str
------- 123.456                 int或float
------- true/false              True/False
------- null                    None
"""


"""将Py对象变成一个JSON以存储数据
使用json.dumps()或者json.dump()
json.dumps()返回一个内容是标准JSON的str
json.dump()把JSON写入一个file-like Object"""
# ——> number_writer.py


"""把JSON反序列化为Py对象
使用对应的json.loads()或者json.load()
json.loads()把JSON的字符串反序列化
json.load()从file-like Object中读取字符串并反序列化"""
# ——> number_reader.py


"""保存和读取用户生成的数据
如果不以某种方式存储用户数据，等程序停止运行时用户的信息将丢失
用户首次运行程序时提示输入用户名并进行存储,再次运行显示欢迎信息"""
# ——> remember_me.py


"""重构 —— 
    -将代码划分为一系列完成具体工作的函数，让代码更清晰、更易于理解、更容易扩展"""
'''对remember_me.py进行重构,将大部分逻辑放到 greet_user() 函数中：'''
# ——> new_remember_me.py
'''对 greet_user() 函数进行重构,让它不执行这么多任务：'''
# ——> new_greet_user.py
'''在 new_greet_user.py 这个最终版本中,每个函数都执行单一而清晰的任务.

执行代码时调用 greet_user()，它打印一条合适的消息：要么欢迎老用户回来，要么问候新用户
greet_user()首先调用get_stored_username()，负责获取存储的用户名（如果存储了的话）
再在必要时调用get_new_username()，负责获取并存储新用户的用户名
要编写出清晰而易于维护和扩展的代码，这种划分工作必不可少
'''