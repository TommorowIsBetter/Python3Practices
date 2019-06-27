#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/6/27 20:52
"""
import itertools
list1 = [1, 2, 3]
# 列表里面的元素组合
combination = itertools.combinations(list1, 2)
print(list(combination))
permutation = itertools.permutations(list1, 2)
print(list(permutation))
