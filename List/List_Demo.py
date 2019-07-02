#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/6/27 20:52
"""
import itertools
from functools import reduce
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

# 传入一个包含字符串的列表，变成数值型列表
numbers = ['1', '5', '10', '8']
numbers = eval('['+(','.join(numbers))+']')
print(numbers)


# 多个不同的列表，生成多个列表的组合
fn = lambda x, code=',': reduce(lambda x, y: [str(i)+code+str(j) for i in x for j in y], x)
list_a = [1, 3, 6]
list_b = [2, 4, 8]
list_c = [5, 7, 9]
list_all = [list_a, list_b, list_c]
# 这里直接调用fn函数，第一个参数代表的是包含多个子列表的列表，第二个参数是分隔符
list_permutation = fn(list_all, '')
for permutation_parameter in list_permutation:
    list_parameter = list(permutation_parameter)
    # 把具有字符串的列表变为数值型的列表
    list_parameter = eval('[' + (','.join(list_parameter)) + ']')
    print(list_parameter)
