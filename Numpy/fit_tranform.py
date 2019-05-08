#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/8 21:10
"""
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
wine = load_wine()
print wine.target
print wine.data.shape
x_train, x_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3)
sc = StandardScaler()
# 根据对之前部分trainData进行fit的整体指标，对剩余的数据（testData）使用同样的均值、方差、最大最小值等指标进行
# 转换transform(testData)，从而保证train、test处理方式相同。
sc.fit_tranform(x_train)
sc.tranform(x_test)
