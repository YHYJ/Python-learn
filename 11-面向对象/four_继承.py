#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""如果要编写的类是现成类的其他版本，可使用 【继承】 .

原有的类称为 【父类/基类/超类】 ，新类称为 【子类】 ;
子类继承父类的所有属性和方法，并且可以定义自己的属性和方法.
"""

print("*"*25 + "子类的__init__()方法" + "*"*25)
#创建子类的实例时首先要给父类所有属性赋值。因此，子类的__init__()方法需要父类施以援手
class Car:        #创建子类时，父类必须包含在当前文件且位于子类前面

    """简单的汽车类作为父类"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 15

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = '出厂日期：' + str(self.year) + '；制造商：' + self.make + '；型号：' + self.model
        return long_name.title()

    def update_odometer(self,mileage):
        """
        将里程表数值odometer_reading设置为指定数值
        禁止回调数值
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("不允许私自篡改行驶里程！")
        print("这辆车已行驶 " + str(self.odometer_reading) + " 公里.")

    def increment_odometer(self,miles):
        """将里程表读数递增"""
        if miles >= self.odometer_reading:
            self.odometer_reading += miles
        else:
            print("不允许私自篡改行驶里程！")

    def fill_gas_tank(self):
        """描述汽车的油箱"""
        print("这辆车有一个容量70L的油箱")


class ElectricCar(Car):     #定义子类时，必须在括号中指定父类的名称
    """父类汽车的子类电动汽车"""

    def __init__(self,make,model,year): #__init__()方法接受创建Car实例所需的信息
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车独有的属性
        """
        #调用ElectricCar的父类的方法__init__()，让ElectricCar实例包含父类的所有属性
        super().__init__(make,model,year)   #父类也称为超类，super因此得名。super()是一个特殊函数，将父类和子类关联起来
        self.battery_size = 70    #子类 【独有的】 属性——电动汽车的电瓶

    #定义子类独有的方法
    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("这辆车有一个 " + str(self.battery_size) + "-KWh 的电瓶.")

    #重写父类的方法——方法fill_gas_tank()是描述油箱的方法，对电动汽车毫无意义，因此想要在电动车子类重写它
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("电动汽车要什么油箱！")

print("*"*25 + "子类继承父类的属性并重新赋值" + "*"*25)
#创建一辆电动车
my_tesla = ElectricCar(make='tesla',model='model s',year=2016)

print("*"*25 + "子类继承父类的方法" + "*"*25)
#
print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(mileage=250)

print("*"*25 + "定义子类独有的方法" + "*"*25)
#
my_tesla.describe_battery()

print("*"*25 + "子类继承父类的方法" + "*"*25)
#重写该方法后对电动汽车调用该方法，将忽略Car类中的fill_gas_tank
my_tesla.fill_gas_tank()    # 转而使用子类中重写的方法，但不会影响父类中的fill_gas_tank.