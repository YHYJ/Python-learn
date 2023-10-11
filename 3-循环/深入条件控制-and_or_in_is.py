#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""在 while 和 if 语句中用到的条件可以包含任何操作符而不仅仅是比较运算符"""

# and、or、in
age_0 = 18
age_1 = 20
'''and——两边都为True'''
print(age_0 <= 20 and age_1 == 20)
'''or——至少一边为True'''
print(age_0 == 18 or age_1 == 18)
'''(not)in——检查特定值是否(不)包含在列表中'''
foods = ['鸡', '鸭', '鱼']
print('鱼' in foods)  # True
print('虾' in foods)  # False
print('蟹' not in foods)  # True

print('*'*50)


# 操作符 is 和 is not 用来比较两个对象是否真正相同
print((1, 2) is (1, 2))   # 两个元组在内存中的地址不一样，所以False
print(id([1, 2]) == id([1, 2]))   # 比较对象为不可变对象才是True
'''当不给序列命名时，序列用完是即时销毁的.

is 是两个对象顺序生成放在栈里比较，地址肯定不同
id 首先生成一个对象a并计算其地址，完成后销毁就没有对象指向a了，a占用的内存空间被释放
然后生成对象b，如果a和b占用的内存大小一样，b会重用原来a的地址，所以是True
'''
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
print(id(a) == id(b))
'''对临时的中间变量做id是没有意义的，is表达式也是一样的.

只有在对象不会被销毁的前提下，才能用 id 来比较两个对象。
所以要把两个表达式的结果绑定到名字上，再来比是不是同一个对象，才能得到正确的结果
'''

print('*'*100)


str1, str2, str3 = '1', '', '0'
non = str1 or str2 or str3  # 取第一个不为空的值，注意空格不为空
ana = str1 and str2 and str3    # 取第一个空值前向左数第一个值，若无空值取最后一个值，注意空格不为空
print(non)
print('1'+ana+'2')
