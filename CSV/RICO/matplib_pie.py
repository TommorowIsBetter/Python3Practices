#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/10/18 17:07
"""
import matplotlib.pyplot as plt

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
labels = ['身份类', '搜索类', '自由类', '数字类']
sizes = [57, 22, 11, 1]
explode = (0.05, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
# plt.title("输入项类别分布")
plt.legend(loc='lower right')
plt.show()
