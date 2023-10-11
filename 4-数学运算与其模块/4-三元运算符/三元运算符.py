#!/usr/bin/env python3
# -*- coding: utf-8 -*-


x = 5
y = 9
if x < y:
    small = x
else:
    small = y
print(small)

print()

small = x if x < y else y
print(small)
