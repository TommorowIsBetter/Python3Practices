#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/6/27 20:52
"""
import itertools
import random
from functools import reduce
from collections import Counter
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
list_c = [5, 7, 69]
list_all = [list_a, list_b, list_c]
# 这里直接调用fn函数，第一个参数代表的是包含多个子列表的列表，第二个参数是分隔符
list_permutation = fn(list_all, ',')
print(list_permutation)
for list_A in list_permutation:
    list_A = list_A.split(",")
    list_A = list(map(int, list_A))
    print(list_A)


# 这里主要是为了解决类别不平衡问题，删除部分类别较多的项目
list_input_ = [[12, 11], [10, 10], [33, 22], [12, 45], [8, 9], [22, -1], [44, 88], [50, 50]]
list_label_ = [2, 2, 2, 2, 1, 2, 3, 3]


# 求重复的某个元素的索引值
def unique_index(L, f):
    """L表示列表， i表示索引值，v表示values，f表示要查找的元素 """
    return [i for (i, v) in enumerate(L) if v == f]


def delete_repeat(list_input, list_label):
    # 统计列表中每个元素出现的个数,并且以字典形式保存
    res = dict(Counter(list_label))
    list_value = sorted(res.items(), key=lambda item: item[1])
    # 输入待测试重复数字
    list_index = unique_index(list_label, 2)
    # 输入待组合的元素数量
    combination = itertools.combinations(list_index, list_value[-1][1] - list_value[-2][1])
    list_combination = list(combination)
    list_len = len(list_combination)
    random_number = random.randint(0, list_len - 1)
    del_list = list_combination[random_number]
    new_list_input = []
    new_list_label = []
    for i in range(len(list_input)):
        if not(i in del_list):
            new_list_input.append(list_input[i])
            new_list_label.append(list_label[i])
    list_input = new_list_input
    list_label = new_list_label
    return list_input, list_label


print(delete_repeat(list_input_, list_label_))

# 删除多个指定位置的列表
list_test = [2, 1, 4, 5, 8, 12]
remove_index = [1, 2, 5]
new_list = []
for i in range(len(list_test)):
    if not(i in remove_index):
        new_list.append(list_test[i])
list_test = new_list
print(list_test)
