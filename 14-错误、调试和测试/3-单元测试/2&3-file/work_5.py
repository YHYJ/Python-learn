#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""雇员：

编写一个名为 Employee 的类：
其方法__init__()接受名、姓和年薪，并将它们都存储在属性中。
编写一个名为 give_raise()的方法，它默认将年薪增加 5000
美元，但也能够接受其他的年薪增加量
"""

class Employee():
    """雇员姓名年薪资料"""

    def __init__(self,firstname,lastname,salary):
        self.firstname = firstname  #姓
        self.lastname = lastname    #名
        self.salary = salary        #年薪

    def give_raise(self,salary_add=5000):
        annual_salary = self.firstname + ' ' + self.lastname \
                        + "原来年薪是" + str(self.salary) \
                        + "，现在是" + str(self.salary + salary_add)
        return annual_salary

#anna = Employee(firstname='安',lastname='娜',salary=100000)
#print(anna.give_raise(salary_add=8000))