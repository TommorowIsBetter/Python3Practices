#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/2/8 16:04
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 设置matplotlib正常显示中文和负号,用黑体显示中文
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# 正常显示负号
matplotlib.rcParams['axes.unicode_minus'] = False
# 随机生成（10000,）服从正态分布的数据
data = [-88.5, 19, 33, 89, 90, 34, 78, 89.3, 99.1, 78.9]
print(data)
"""
绘制直方图
data:必选参数，绘图数据
bins:直方图的长条形数目，可选项，默认为10
normed:是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率。
facecolor:长条形的颜色
edgecolor:长条形边框的颜色
alpha:透明度
"""
# plt.hist(data, bins=range(0, 101, 1), density=1, facecolor="blue", edgecolor="black", alpha=0.7)
plt.hist(data, density=0, facecolor="blue", edgecolor="black", alpha=0.7)
# 显示横轴标签
plt.xlabel("区间")
# 显示纵轴标签
plt.ylabel("频数/频率")
# 显示图标题
plt.title("频数/频率分布直方图")
plt.show()