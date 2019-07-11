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
list_input = [[12, 11], [33, 22], [12, 45], [8, 9], [22, -1], [44, 88]]
list_label = [2, 2, 2, 1, 2, 3]
# 统计列表中每个元素出现的个数,并且以字典形式保存
res = dict(Counter(list_label))
print(res)


# 求重复的某个元素的索引值
def unique_index(L, f):
    """L表示列表， i表示索引值，v表示values，f表示要查找的元素 """
    return [i for (i, v) in enumerate(L) if v == f]


# 输入待测试重复数字
list_index = unique_index(list_label, 2)
print(list_index)
# 输入待组合的元素数量
combination = itertools.combinations(list_index, 3)
list_combination = list(combination)
print(list_combination)
list_len = len(list_combination)
print('list_len', list_len)
random_number = random.randint(0, list_len - 1)
print("随机数的值：", random_number)
del_list = list_combination[random_number]
print(del_list)
for i in del_list:
    del list_input[i]
    del list_label[i]
print(list_input)
print(list_label)
