#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/29 18:46
"""
from sklearn.datasets import load_boston
from sklearn.feature_selection import SelectKBest, f_regression
boston = load_boston()
X, y = boston.data, boston.target
print(X.shape)
X_new = SelectKBest(f_regression, k=6).fit_transform(X, y)
print(X_new.shape)
