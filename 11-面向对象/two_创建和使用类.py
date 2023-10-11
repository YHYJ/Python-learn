#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用类几乎可以模拟任何东西"""


'''编写一个Dog类,包含狗的两项信息（名字和年龄）和两种行为（蹲下和打滚）
Dog类让Python知道如何创建表示小狗的对象.
编写这个类后，将使用它来创建表示特定小狗的实例.
'''

print("*"*25 + "创建Dog类" + "*"*25)
# 根据Dog类创建的每个实例都将存储名字(name)和年龄(age)，赋予了每条小狗蹲下(sit())和打滚(roll_over())的能力
class Dog():    # 定义名为 Dog 的类，Python约定类名首字母大写。从空白创建类，所以括号为空
    """模拟犬类"""  # 类功能的描述

    def __init__(self,name,age):    # __init__() 是一个特殊的方法，每当根据Dog类创建新实例时，Py都会自动运行它
        """初始化属性name和age"""     # 形参中，self 必不可少且必须位于其他形参前面(因为self就指向创建的实例本身)
        self.name = name    # 以self为前缀的变量都可供类中的所有方法使用，并可以通过类的任何实例访问这些变量
        self.age = age      # self.name = name 获取存储在形参name中的值并将之存储到变量name中，然后该变量被关联到当前创建的实例
        # 像这样可以通过实例访问的变量称为【属性】

    def sit(self):      #类的sit()方法
        """模拟犬类接受命令蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):    #类的roll_over()方法
        """模拟犬类接受命令打滚"""
        print(self.name.title() + " rolled over!")


print("*"*25 + "根据类创建实例" + "*"*25)
# 可将类视为关于如何创建实例的说明。Dog类是一系列说明，让Py知道如何创建表示特定小狗的实例。
my_dog = Dog(name='傻狗',age=6)   #创建6岁叫'傻狗'的小狗，Py使用'傻狗'和6调用Dog类中的方法__init__()
                                 # 创建一个表示特定小狗的实例，并使用提供的实参设置属性 name 和 age ，
                                 # 方法__init__()并未显式的包含return语句，但Py自动返回一个表示这条小狗的实例

print("My dog's name is " + my_dog.name.title() + "," +     #访问实例的属性 用句点表示法，如 my_dog.name
      "it's " + str(my_dog.age) + " years old.")    #先找到实例 my_dog ,再依次查找相关联的属性name

my_dog.sit()    # 调用Dog类中定义的方法sit()和roll_over()，也使用句点表示法，格式：<实例名>.<方法名>
my_dog.roll_over()  # 遇到代码my_dog.sit()时， Py在类Dog中查找方法sit()并运行其代码

your_dog = Dog(name='二狗',age=3)    # 创建多个实例——可按需求根据类创建任意数量的实例
her_dog = Dog(name='ZZ狗',age=2)    # 创建‘二狗’和‘ZZ狗’，每条小狗都是独立的实例，有自己的一组属性，能执行相应的操作
print("Your dog's name is " + your_dog.name.title() + "," +
      "it's " + str(your_dog.age) + " years old.")
your_dog.sit()
print("Her dog's name is " + her_dog.name.title() + "," +
      "it's " + str(her_dog.age) + " years old.")
her_dog.roll_over()
'''就算给第二条小狗指定同样的名字和年龄， Python依然会根据Dog类创建另一个实例.

可按需求根据一个类创建任意数量的实例，条件是将每个实例存储在不同的变量中，或占用列表或字典的不同位置
'''