#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 遍历遍历所有键-值对:
print('*'*25 + '遍历所有键值对' + '*'*25)
'''items()方法返回一个键值对列表依次存储到key,value'''
for key, name in favorite_languages.items():
    print("名字:" + key)
    print("最喜欢的语言:" + name, '\n')


# 遍历所有键:
print('*'*25 + '遍历所有键' + '*'*25)
for name in favorite_languages.keys():
    print(name.title())
'''遍历字典时，默认会遍历所有的键.
因此，如果将上述代码中的for name in favorite_languages.keys():
替换为for name in favorite_languages:，输出不变'''
'''在这种循环中.可使用当前键来访问与之相关联的值'''
for name in favorite_languages.keys():
    print(name.title().ljust(8) + '最喜欢的是：' + favorite_languages[name].title())

'''使用sorted()方法进行排序遍历所有键'''
for name in sorted(favorite_languages.keys()):
    print(name.title().ljust(8) + "感谢接受调查！")


# 遍历所有值
print('*'*25 + '遍历所有值' + '*'*25)
for value in sorted(favorite_languages.values()):
    print(value.title())    # 未考虑重复
print("备选语言有：")
# 使用set消除重复元素,set最大的作用就是去重
for value in sorted(set(favorite_languages.values())):
    print(value.title())
