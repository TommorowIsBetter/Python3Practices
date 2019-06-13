#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/6/13 16:42
"""


# 两个列表元素的相对误差，然后精确度
def relative_accuracy(list_1, list_2):
    sum_ = 0.0
    for list_value_1, list_value_2 in zip(list_1, list_2):
        sum_ += 1 - abs(list_value_1 - list_value_2) / list_value_1
    accuracy = sum_ / len(list_1)
    accuracy_value = str('%.2f' % (accuracy * 100)) + '%'
    return accuracy_value


# 两个列表元素的绝对误差
def absolute_accuracy(list_1, list_2):
    sum_ = 0.0
    for list_value_1, list_value_2 in zip(list_1, list_2):
        sum_ += abs(list_value_1 - list_value_2)
    accuracy = sum_ / len(list_1)
    return accuracy


a = [1, 2, 4, 1, 3]
b = [1, 4, 2, 8, 3]
print(relative_accuracy(a, b))
print(absolute_accuracy(a, b))
c = 0.125777966
# 显示方式：下划线 前景色：绿色 背景色：白色背景
print("\033[1;32;41m" + str(round(c, 2)) + "\033[0m")
