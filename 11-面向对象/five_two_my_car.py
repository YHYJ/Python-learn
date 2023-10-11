#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from five_one_car import Car     #打开模块car并导入其中的Car类

my_car = Car(make='audi',model='a4',year='2016')
print(my_car.print_car_info())

my_car.odometer_reading = 23
my_car.read_odometer()