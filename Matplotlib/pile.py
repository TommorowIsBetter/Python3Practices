#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/10 10:30
"""
import matplotlib.pyplot as plt
import numpy as np
# 给出在y轴上的位置
x = np.arange(5)
# 给出具体每个直方图的数值
y = np.array([5, 4, 7, 2, 9])
# 给出第二组直方图信息
y1 = np.array([3, 5, 2, 4, 10])
# 给出第三组数据
y2 = np.array([3, 4, 6, 2, 5])

plt.bar(x, y, label='workday')
plt.bar(x, y1, bottom=y, label='weekend')
plt.bar(x, y2, bottom=y+y1, label='Christmas')
# 列出图例
plt.legend()
plt.show()
