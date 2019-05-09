#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/9 15:45
"""
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor


# 获取boston房价数据集
def get_boston_dataset():
    boston = load_boston()
    return boston.data, boston.target


# 用knn平均回归算法进行预测
def train_by_knn_regressor_uniform():
    input, target = get_boston_dataset()
    x_train, x_test, y_train, y_test = train_test_split(input, target, test_size=0.3, random_state=33)
    ss_x = StandardScaler()
    x_train = ss_x.fit_transform(x_train)
    x_test = ss_x.transform(x_test)
    ss_y = StandardScaler()
    y_train = ss_y.fit_transform(y_train.reshape(-1, 1))
    y_test = ss_y.transform(y_test.reshape(-1, 1))
    uniform_knn = KNeighborsRegressor(weights='uniform')
    uniform_knn.fit(x_train, y_train)
    accuracy = uniform_knn.score(x_test, y_test)
    print("accuracy:", accuracy)


# 用knn距离加权回归算法进行预测
def train_by_knn_regressor_distance():
    input, target = get_boston_dataset()
    x_train, x_test, y_train, y_test = train_test_split(input, target, test_size=0.3, random_state=33)
    ss_x = StandardScaler()
    x_train = ss_x.fit_transform(x_train)
    x_test = ss_x.transform(x_test)
    ss_y = StandardScaler()
    y_train = ss_y.fit_transform(y_train.reshape(-1, 1))
    y_test = ss_y.transform(y_test.reshape(-1, 1))
    uniform_knn = KNeighborsRegressor(weights='distance')
    uniform_knn.fit(x_train, y_train)
    accuracy = uniform_knn.score(x_test, y_test)
    print("accuracy:", accuracy)


train_by_knn_regressor_uniform()
train_by_knn_regressor_distance()