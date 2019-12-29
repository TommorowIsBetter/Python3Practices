#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/29 21:34
"""
from sklearn.svm import SVR
from sklearn.datasets import load_boston
from sklearn.feature_selection import SelectFromModel
boston = load_boston()
X, y = boston.data, boston.target
print(X.shape)
lsvr = SVR(kernel="linear").fit(X, y)
model = SelectFromModel(lsvr, prefit=True)
X_new = model.transform(X)
print(X_new)
print(X_new.shape)
print("被选中的特征：", boston.feature_names[model.get_support()])

