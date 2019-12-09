#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/9 13:32
"""
from sklearn.feature_selection import VarianceThreshold
X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
print(type(X))
print(X)
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
X = sel.fit_transform(X)
print(type(X))
print(X)
