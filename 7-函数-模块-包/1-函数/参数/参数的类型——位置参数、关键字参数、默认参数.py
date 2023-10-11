#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""参数的调用.
调用参数时，必须将实参都关联到形参.
"""


# 位置参数
print("*"*25 + "位置参数" + "*"*25)
def describe_pet(animal_type, pet_name):
    """
    显示宠物的信息
    :param animal_type:
    :param pet_name:
    :return:
    """
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")

describe_pet('鹦鹉', '2333')   # 调用时需要按照顺序提供宠物类型和名字
describe_pet('八哥', '8brother')


# 关键字参数
print("*"*25 + "关键字参数" + "*"*25)
'''关键字参数是传递给函数的【名称-值】对.
直接在实参中将名称和值进行关联，因此不会混淆并清晰指出各个参数的作用'''
describe_pet(pet_name='KJ', animal_type='柯基')   # 用关键字参数调用describe_pet()函数


# 默认值
print("*"*25 + "默认值" + "*"*25)
'''给每个形参指定默认值，调用函数时，未提供实参将使用默认值
如describe_pet()函数设置 animal_type 参数默认值为 'dog' '''
def describe_pet(pet_name, animal_type = 'dog'):  # 需要将不指定默认值的形参放在列表开头
    """
    显示宠物的信息
    :param pet_name:
    :param animal_type:
    :return:
    """
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")

describe_pet(pet_name='wahaha')  # 不给定 animal_type 参数，使用默认值
describe_pet(animal_type='狗子', pet_name='GZ')
'''在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参
这让Py依然能够正确地解读位置实参
'''


# 使参数可选
'''为让形参可选，可给该形参指定默认值为空字符串
并在用户没有提供该参数时不使用'''
def get_formatted_name(first_name, middle_name='', last_name=''):
    """
    返回整洁的姓名（可能包含中间名）
    :param first_name:
    :param middle_name:
    :param last_name:
    :return:
    """
    if middle_name:   # 如果提供中间名
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
myname = get_formatted_name('jim', 'lee')
print(myname)
myname = get_formatted_name('pig', 'lyb', 'ff')
print(myname)
