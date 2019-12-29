#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/29 18:36
@description: 移除低方差特征
"""
from sklearn.feature_selection import VarianceThreshold
X = [[0, 0, 1],
     [0, 1, 0],
     [1, 0, 0],
     [0, 1, 1],
     [0, 1, 0],
     [0, 1, 1]]
sel = VarianceThreshold(threshold=(0.8*(1-0.8)))
X = sel.fit_transform(X)
print(X)
