#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/29 19:38
"""
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
# Load boston housing dataset as an example
from sklearn.feature_selection import SelectFromModel

boston = load_boston()
X = boston["data"]
Y = boston["target"]
names = boston["feature_names"]

rf = RandomForestRegressor(n_estimators=20, max_depth=4)
clf = rf.fit(X, Y)
print(clf.feature_importances_)
model = SelectFromModel(clf, threshold=0.01, prefit=True)
X_new = model.transform(X)
print(X_new.shape)
print("被选中的特征：", boston.feature_names[model.get_support()])

