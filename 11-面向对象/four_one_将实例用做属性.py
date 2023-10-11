#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''将实例用做属性——

随着给类添加的细节越来越多：属性和方法的清单以及文件越来越长.
需要将类的一部分作为一个独立的类提取出来：将大型类拆分成多个协同工作的小类.
例如：将ElectricCar类中专门针对汽车电瓶的属性和方法提取出来，放到另一个名为Battery的类中，
并将一个Battery实例用作ElectricCar类的一个属性.
'''

print("*"*25 + "将实例用做属性" + "*"*25)
#创建一个名为Battery的类并将一个Battery实例用作ElectricCar类的一个属性.
class Car():
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


class Battery():       #定义一个新类 Battery ，不继承于任何类
    """模拟电动汽车电瓶"""

    def __init__(self,battery_size = 100):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("这辆车配置一个容量为 " + str(self.battery_size) + "-KWh 的电瓶.")

    def get_ranges(self):
        """打印消息，指出电瓶续航里程"""
        if self.battery_size >= 150:
            message = "这辆车在满电情况下的续航里程是 300+ 千米."
        elif self.battery_size < 150 and self.battery_size >= 100:
            message = "这辆车在满电情况下的续航里程是 100~130 千米."
        elif self.battery_size < 100:
            message = "该车电瓶容量不合格！"

        print(message)


class ElectricCar(Car):
    """汽车类的子类电动汽车"""

    def __init__(self,make,model,year):
        """初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make,model,year)
        # 创建一个Battery实例存储到属性 self.battery
        self.battery = Battery(battery_size=120)    #指定Battery实例的形参 battery_size = 100
        #每当__init__()被调用时，都将执行该操作；因此每个ElectricCar实例都包含一个自动创建的Battery实例

my_tesla = ElectricCar(make='tesla',model='model s',year=2017)  #创建电动汽车my_tesla
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()     #描述电瓶，要用到ElectricCar的属性battery
# 该代码让Py在实例my_tesla中查找属性battery，并调用存储在Battery实例中的方法describe_battery()
my_tesla.battery.get_ranges()