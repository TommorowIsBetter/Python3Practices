#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/8 18:58
"""


from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
wine = load_wine()
print wine.target
print wine.data.shape
x_train, x_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3)
# 决策树实例
clf = DecisionTreeClassifier(random_state=0)
# 随机森林实例
rfc = RandomForestClassifier(random_state=0)
clf = clf.fit(x_train, y_train)
rfc = rfc.fit(x_train, y_train)
score_c = clf.score(x_test, y_test)
score_r = rfc.score(x_test, y_test)
print score_c, score_r
