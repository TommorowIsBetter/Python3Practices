#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/9 15:52
"""
from sklearn.datasets import load_breast_cancer
from sklearn.feature_selection import GenericUnivariateSelect, chi2
X, y = load_breast_cancer(return_X_y=True)
print(X.shape)
# chi2代表的是分类任务，‘k_best’代表的是使用SelectKBest方法
transformer = GenericUnivariateSelect(chi2, 'k_best', param=20)
X_new = transformer.fit_transform(X, y)
print(X_new.shape)
