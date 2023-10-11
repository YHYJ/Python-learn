#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from five_five_electric_car import ElectricCar

my_tesla_car = ElectricCar(make='tesla',model='model s',year='2018')

print(my_tesla_car.print_car_info())
my_tesla_car.battery.print_battery()
my_tesla_car.battery.get_range()