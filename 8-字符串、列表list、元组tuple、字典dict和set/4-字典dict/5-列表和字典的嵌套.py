#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('*'*25 + '当需要在列表中存储多个个体时，可以在列表中嵌套多个字典' + '*'*25)

'''在列表中存储字典.

创建一个外星人列表,其中每个外星人都是一个字典，包含该外星人各种信息.
'''
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
print('*'*25+'外星人不止3个切由代码自动生成，使用range()'+'*'*25)
#创建一个空列表用来存储外星人：
aliens = []
#创建红黄绿各10个外星人：
for alien_number in range(10):
    new_alien_0 = {'color':'red','points':15,'speed':'速度快'}
    new_alien_1 = {'color':'yellow','points':10,'speed':'速度中'}
    new_alien_2 = {'color':'green','points':5,'speed':'速度慢'}
    aliens.append(new_alien_0)
    aliens.append(new_alien_1)
    aliens.append(new_alien_2)
#显示前5个：
for alien in aliens[:5]:
    print(alien)
print("……")
#显示创建了多少个外星人：
print("外星人总数为：" + str(len(aliens)))


print('*'*25 + '当需要存储一个个体的多个属性时，可以在字典中嵌套一个列表' + '*'*25)

'''在字典中存储列表.

'''
#存储所点披萨的信息：
pizza = {
    'crust':'厚',
    'toppings':['洋葱','火腿','芝士'],
}
#概述所点的披萨：
print("你点了一个" + pizza['crust'] + "的披萨" +
      "，配料为：")
for topping in pizza['toppings']:
    print("\t" + topping)
print('*'*25 + '最喜欢的语言' + '*'*25)
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name,languages in favorite_languages.items():
    print(name.title() + "最喜欢的语言是：")
    for language in languages:
        print("\t" + language.title())
    print()


print('*'*25 + '当需要存储多个个体的多个属性时，可以在字典中嵌套字典' + '*'*25)

users = {
    'aeinstein':{'first':'albert','last':'einstein','location':'princeton',},
    'mcurie':{'first':'marie','last':'curie','location':'paris',},
}
for username,user_info in users.items():
    print("Username:" + username.title())

    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name:" + full_name.title())
    print("\tLocation:" + location.title() + '\n')


'''创建一个名为 cities 的字典，其中将三个城市名用作键.

对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实.
在表示每座城市的字典中，应包含 country、 population 和 fact 等键.
将每座城市的名字以及有关它们的信息都打印出来.
'''
cities = {
    'beijing':{'contry':'china','population':'1000000','fact':'京都',},
    'nanjing':{'contry':'china','population':'800000','fact':'六朝古都',},
    'qingdao':{'contry':'china','population':'600000','fact':'家乡',},
}
print("*"*50 + "第一种表示方法：" + "*"*50)
for city,city_info in sorted(cities.items()):
    print("城市：" + city.title())
    # 通过for循环读取字典　city_info{}　的内容
    for city_contry,city_population in sorted(city_info.items()):
        print(city_contry + ":" + city_population)
    print()

print("*"*50 + "第二种表示方法：" + "*"*50)
for city, city_info in sorted(cities.items()):
    print("城市：" + city.title())
    # 通过3个变量读取字典　city_info{}　的内容
    city_contry = city_info['contry'].title()
    city_population = city_info['population'].title()
    city_fact = city_info['fact'].title()

    print("所属国家:" + city_contry,"人口:" + city_population,"标签:" + city_fact + '\n')