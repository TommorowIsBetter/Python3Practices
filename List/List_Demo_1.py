#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/7/12 22:08
"""
import random
from collections import Counter
# 这里主要是为了解决类别不平衡问题，删除部分类别较多的项目
list_input_ = [[12, 11], [10, 10], [33, 22], [12, 45], [8, 9], [22, -1], [44, 88], [50, 50], [100, 22]]
list_label_ = [2, 4, 2, 1, 1, 2, 3, 3, 4]


# 对一个列表中求重复的某个元素的索引值，并且以列表形式返回
def unique_index(L, f):
    """L表示列表， i表示索引值，v表示values，f表示要查找的元素 """
    return [i for (i, v) in enumerate(L) if v == f]


# 从列表中，随机删除keep_number个元素，被删除的元素放在一个列表中并且返回
def del_index_list(list_del_, keep_number):
    list_new = []
    while keep_number > 0:
        i = random.randint(0, len(list_del_)-1)
        list_new.append(list_del_.pop(i))
        keep_number = keep_number - 1
    return list_new


# 保持数据集列表中的value_a和value_b个数一样多
def balance_list(list_input, list_label, value_a, value_b):
    # 统计列表中每个元素出现的个数,并且以字典形式保存
    res = dict(Counter(list_label))
    if res[value_a] > res[value_b]:
        value_max = value_a
    else:
        value_max = value_b
    # 重复数字2的索引列表
    list_index = unique_index(list_label, value_max)
    del_list = del_index_list(list_index, abs(res[value_a] - res[value_b]))
    new_list_input = []
    new_list_label = []
    for i in range(len(list_label)):
        if not(i in del_list):
            new_list_input.append(list_input[i])
            new_list_label.append(list_label[i])
    list_input = new_list_input
    list_label = new_list_label
    return list_input, list_label


# 对整个不平衡列表数量进行平衡
def balance_list_all(list_input, list_label, value_a, value_b, value_c, value_d):
    list_input, list_label = balance_list(list_input, list_label, value_a, value_b)
    list_input, list_label = balance_list(list_input, list_label, value_a, value_c)
    list_input, list_label = balance_list(list_input, list_label, value_a, value_d)
    list_input, list_label = balance_list(list_input, list_label, value_b, value_c)
    list_input, list_label = balance_list(list_input, list_label, value_b, value_d)
    list_input, list_label = balance_list(list_input, list_label, value_c, value_d)
    return list_input, list_label


print(balance_list_all(list_input_, list_label_, 1, 2, 3, 4))
