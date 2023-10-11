#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""collections是Py内建的一个集合模块，提供了许多有用的集合类"""


from collections import namedtuple, deque, defaultdict
from collections import OrderedDict, Counter

# namedtuple函数——用来创建一个自定义的tuple对象
'''一个点的三维坐标就可以表示成元组例如(2,3,6)
但很难看出这个tuple是用来表示一个坐标的
定义一个class又小题大做了，这时，namedtuple就派上了用场'''
point = namedtuple('Point', ['x', 'y', 'z'])  # namedtuple('名称', [属性list]):
p = point(2, 3, 6)
print(type(p), p)
print(p.x, p.y, p.z)
'''namedtuple的属性规定了tuple里元素的个数
并可以用属性而不是索引来引用tuple的某个元素
用namedtuple可以很方便地定义一种数据类型-
-它具备tuple的不变性，又可以根据属性来引用，使用十分方便'''
# 验证创建的point对象是tuple的一种子类
print(isinstance(p, point))
print(isinstance(p, tuple))


# deque——为了高效实现插入和删除操作的双向列表，适合用于队列和栈
'''使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了-
-因为list是线性存储，数据量大的时候，插入和删除效率很低'''
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(type(q))
print('q的值是：', q)
'''deque除了实现list的append()和pop()外，还支持appendleft()和popleft()
这样就可以非常高效地往头部添加或删除元素'''


# defaultdict——除了在Key不存在时返回默认值，defaultdict的行为跟dict完全一样
'''使用dict时，如果引用的key不存在，就会抛出KeyError
如果希望key不存在时返回一个默认值，可以使用defaultdict'''
dd = defaultdict(lambda: 'N/A')     # 传入函数匿名设置默认值为 'N/A'
dd['key1'] = 'ABC'
print(dd['key1'])   # key1存在，返回其value值
print(dd['key2'])   # key2不存在，返回默认值 'N/A'，默认值是调用函数返回的

# OrderedDict——OrderedDict中的key是有序的
'''使用dict时，Key是无序的，这样对dict迭代就无法确定Key的顺序
如果要保持Key的顺序，可以用OrderedDict'''
d = dict([('a', 1), ('b', 2), ('c', 3)])
print('原始的dict：', d)     # dict的key是无序的
od = OrderedDict([('a', 1), ('c', 3), ('b', 13)])
print(od)
'''OrderedDict的key会按照插入的顺序排序，不是按照key本身'''
od_1 = OrderedDict()
od_1['z'] = 12
od_1['x'] = 18
od_1['w'] = 0
print(list(od_1.keys()))     # 按照插入的key的顺序返回
'''OrderedDict可以实现一个FIFO（先进先出）的dict
当容量超出限制时，先删除最早添加的Key'''
class LastUpdatedOrderedDict(OrderedDict):

    """继承自父类OrderedDict"""
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self.__capacity = capacity   # 私有变量

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self.__capacity:
            last = self.popitem(last=False)  # last参数设置为False则是LIFO顺序，默认True
            print('remove移除', last)
        if containsKey:
            del self[key]
            print('set集合：', (key, value))
        else:
            print('add添加：', (key, value))
        OrderedDict.__setitem__(self, key, value)

# Counter——一个简单的计数器
'''例如，统计字符出现的个数：'''
c = Counter()
for ch in 'programing':
    c[ch] += 1
print(c)
'''Counter实际上也是dict的一个子类'''
