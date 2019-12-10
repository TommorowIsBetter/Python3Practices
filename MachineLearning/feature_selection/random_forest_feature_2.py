#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/10 10:47
"""
from sklearn.datasets import load_boston
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestRegressor
boston = load_boston()
rf = RandomForestRegressor()
X = boston["data"]
print(X.shape)
print(boston["feature_names"])
Y = boston["target"]
rf.fit(X, Y)
print(rf.feature_importances_)
model = SelectFromModel(rf, prefit=True, threshold=0.01)
X_new = model.transform(X)
# 打印被选中的列表
print(model.get_support(indices=True))
print(X_new.shape)
