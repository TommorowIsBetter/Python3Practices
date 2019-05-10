#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/10 17:19
"""

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
boston = load_boston()
x = boston.data
y = boston.target
# 剔除掉顶部值为50的点
x = x[y < 50.0]
y = y[y < 50.0]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=33)
# 这里多元线性回归不需要使用数据标准化
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)
print(lin_reg.score(x_test, y_test))
