#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/10/18 18:45
"""
# 解决中文显示问题
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

stu = np.array(["随机生成英文测试数据", "随机生成中文测试数据", "应用内挖掘测试数据"])
num = np.arange(1, 4)
plt.xticks(num, stu)

search_number_list = [0.8, 0.1, 4.5]
state_number_of_picture_list = [2.1, 1.5, 5]
state_number_of_tree_list = [1.3, 1.2, 2.5]

n = 3
w = 0.8 / n
# 单数个轴用center
plt.bar(num, search_number_list, label='搜索成功数量', color='green', width=w, align='center')
plt.bar(num - w, state_number_of_picture_list, label='图片度量状态数量', color='blue', width=w, align='center')
plt.bar(num + w, state_number_of_tree_list, label='拓扑结构度量状态数量', color='red', width=w, align='center')
plt.legend(loc='upper left')
plt.show()
