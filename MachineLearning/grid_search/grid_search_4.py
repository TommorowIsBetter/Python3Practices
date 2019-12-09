#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/9 13:01
@description:通过sklearn的交叉验证方式
"""
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

iris = load_iris()
# 把要调整的参数以及其候选值列出来
param_grid = {"gamma": [0.001, 0.01, 0.1, 1, 10, 100],
             "C": [0.001, 0.01, 0.1, 1, 10, 100]}
print("Parameters:{}".format(param_grid))
# 实例化一个GridSearchCV类
grid_search = GridSearchCV(SVC(), param_grid, cv=5)
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=10)
# 训练，找到最优的参数，同时使用最优的参数实例化一个新的SVC estimator
grid_search.fit(X_train, y_train)
print("Test set score:{:.2f}".format(grid_search.score(X_test,y_test)))
print("Best parameters:{}".format(grid_search.best_params_))
print("Best score on train set:{:.2f}".format(grid_search.best_score_))
