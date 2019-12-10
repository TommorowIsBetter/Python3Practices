#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/10 10:39
"""
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
boston = load_boston()
X = boston["data"]
print(type(X), X.shape)
Y = boston["target"]
names = boston["feature_names"]
print(names)
rf = RandomForestRegressor()
rf.fit(X, Y)
print("Features sorted by their score:")
print(sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names), reverse=True))