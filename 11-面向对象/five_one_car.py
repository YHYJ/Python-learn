#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""一个可用于表示燃油汽车"""

class Car():
    """模拟汽车"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def print_car_info(self):
        """返回整洁的汽车数据"""
        long_name = "车辆出厂信息：\n" + \
                    "出厂日期： " + str(self.year) +\
                    "\n制 造 商： " + self.make +\
                    "\n型   号： " + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车里程"""
        print("该车已行驶" + str(self.odometer_reading) + "公里.")

    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值
        拒绝回拨里程表数据
        :return:
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("拒绝修改回拨里程表数据")

    def increment_odometer(self,mileage):
        """将里程表读数增加指定的量"""
        self.odometer_reading += mileage