#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/6/6 21:09
"""
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
X = iris.data
Y = iris.target
X = X[:, :]
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.8, test_size=0.2, random_state=20)
clf = svm.SVC(C=0.9, kernel='rbf', gamma=10, decision_function_shape='ovo')
clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))
