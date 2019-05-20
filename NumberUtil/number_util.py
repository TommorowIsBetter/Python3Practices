#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/20 20:19
"""
import math
n = 3.75
# 向下取整数
print(int(n))
# 四舍五入
print(round(n))
# 向下取整,利用math模块的函数
print(math.floor(n))
# 向上取整，利用math模块的函数
print(math.ceil(n))
# 分别取整数部分和小数部分
print(math.modf(n))
