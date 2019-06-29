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
# 列表里面的元素排列
permutation = itertools.permutations(list1, 2)
print(list(permutation))

list2 = [2, 19, 3, 26]
# 打印最大值的位置
print(list2.index(max(list2)))
# 打印最小值的位置
print(list2.index(min(list2)))
