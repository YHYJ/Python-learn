#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Car():
    """模拟汽车"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make        #类中的每个属性都必须有初始值，哪怕这个值是0或空字符串
        self.model = model      #make、model、year属性的初始值是对应的外部传入参数
        self.year = year
        self.odometer_reading = 10   #添加里程属性odometer_reading，初始值设为0

    def get_descriptive_name(self):  #Car()类的方法
        """返回整洁的描述性信息"""
        long_name = '出厂日期：' + str(self.year) + '；制造商：' + self.make + '；型号：' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车行驶里程信息"""
        print("这辆车已行驶 " + str(self.odometer_reading) + " 公里.")

    def update_odometer(self,mileage):
        """
        将里程表数值odometer_reading设置为指定数值
        禁止回调数值
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("不允许私自篡改行驶里程！")

    def increment_odometer(self,miles):
        """将里程表读数递增"""
        if miles >= self.odometer_reading:
            self.odometer_reading += miles
        else:
            print("不允许私自篡改行驶里程！")

my_car = Car(make='audi',model='a4',year=2017)
print(my_car.get_descriptive_name())
my_car.read_odometer()

your_car = Car(make='subaru',model='outback',year=2013)
print(your_car.get_descriptive_name())
your_car.odometer_reading = 2        #1.通过实例直接修改属性的值
your_car.read_odometer()
your_car.update_odometer(mileage=25)  #2.通过update_odometer()方法修改属性的值
your_car.read_odometer()
your_car.increment_odometer(miles=-100)  #3.通过方法对属性的值进行递增
your_car.read_odometer()