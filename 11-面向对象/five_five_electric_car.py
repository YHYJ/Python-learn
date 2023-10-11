#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""一个表示电动汽车的类"""

from five_one_car import Car     #ElectricCar类需要访问其父类Car，因此将Car类导入

class Battery():
    """模拟电动汽车电瓶"""

    def __init__(self,battery_size=60):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def print_battery(self):
        """描述电瓶容量容量"""
        print("该车电瓶容量： " + str(self.battery_size) + "-KWh")

    def get_range(self):
        """描述电池可续航里程"""
        if self.battery_size >= 85:
            range = 240
        else:
            range = 190
        message = "该车满电续航： " + str(range) + "公里."
        print(message)


class ElectricCar(Car):
    """模拟电动车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类的属性，再初始化电动车独有的属性"""
        super().__init__(make,model,year)
        self.battery = Battery(battery_size=250)