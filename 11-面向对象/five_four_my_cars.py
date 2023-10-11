#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("*"*25 + "导入多个类" + "*"*25)
#from car import Car,ElectricCar

from five_one_car import Car
from five_five_electric_car import ElectricCar

my_battle_car = Car(make='大众汽车公司',model='甲壳虫',year=1996)    #普通车
print(my_battle_car.print_car_info())

my_tesla_car = ElectricCar(make='特斯拉',model='跑车',year=2020)    #电动车
print(my_tesla_car.print_car_info())



print("*"*25 + "导入整个模块" + "*"*25)
import five_one_car
import five_five_electric_car

my_beetle = five_one_car.Car(make='volkswagen',model='beetle',year=2016)
print(my_beetle.print_car_info())

my_tesla = five_five_electric_car.ElectricCar(make='tesla',model='roadster',year=2016)
print(my_tesla.print_car_info())