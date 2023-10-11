#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""城市和国家：

编写一个函数，它接受两个形参：一个城市名和一个国家名。这
个函数返回一个格式为 City, Country 的字符串，如 Santiago, Chile.
"""


def city_function(city, country, population=''):
    if population:
        city_country = city + ',' + country + \
            ' - population ' + str(population)
    else:
        city_country = city + ',' + country
    return city_country.title()
