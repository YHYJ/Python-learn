#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Python允许将类存储在模块中，然后在主程序中导入所需模块."""


print("*"*25 + "导入单个类" + "*"*25)
#1.创建 five_one_car.py 模块，只包含Car类 ——> five_one_car.py
#2.创建 five_two_my_car.py ，在其中导入Car类并创建其实例 ——> five_two_my_car.py


print("*"*25 + "在一个模块中存储多个类" + "*"*25)
#可根据需要在一个模块中存储任意数量的类
#1.将Battery和ElectricCar都加入到模块 five_one_car.py ——> five_one_car.py
#2.新建 five_three_my_electric_car.py ，导入ElectricCar类并创建一辆电动车 ——> five_three_my_electric_car.py


print("*"*25 + "从一个模块中导入多个类" + "*"*25)
#可根据需要在程序文件中导入任意数量的类
#1.将Car和ElectricCar类都导入，以在同一个程序中创建普通汽车和电动汽车 ——> five_four_my_cars.py


print("*"*25 + "导入整个模块" + "*"*25)
#可以导入整个模块，再使用句点表示法访问需要的类，方法简单代码易阅读.
#1.由于创建类实例的代码都包含模块名，不会与当前文件使用的任何名称发生冲突 ——> five_four_my_cars.py


print("*"*25 + "导入模块中的所有类" + "*"*25)
# form car import *
#不推荐使用
# 1.没有明确地指出导入了模块中的哪些类
# 2.如果不小心导入了一个与程序文件中其他东西同名的类，将引发难以诊断的错误


print("*"*25 + "在一个模块中导入另一个模块" + "*"*25)
#将类存储在多个模块中时，会发现一个模块中的类依赖于另一个模块中的类
#1.这种情况下可在前一个模块中导入必要的类
#2.将Car类存储在一个模块中，并将ElectricCar和Battery类存储在另一个模块中 ——> five_five_electric_car.py
#3.因为ElectricCar类需要访问其父类Car，因此将Car类导入到 five_five_electric_car.py 模块中
#4.还需要更新模块five_one_car.py，使其包含Car类：