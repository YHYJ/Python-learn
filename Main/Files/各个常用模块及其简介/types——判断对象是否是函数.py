#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import types


def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(i for i in range(10)) == types.GeneratorType)


# 最好用isinstance()函数
print(isinstance(fn, types.FunctionType))
print(isinstance(abs, types.BuiltinFunctionType))
print(isinstance(lambda x: x, types.LambdaType))
print(isinstance((i for i in range(10)), types.GeneratorType))
