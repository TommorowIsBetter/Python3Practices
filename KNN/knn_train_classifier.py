#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/9 15:13
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


# 获取鸢尾花数据集
def get_iris_dataset():
    iris = load_iris()
    return iris.data, iris.target


def train_by_knn():
    iris_data, iris_target = get_iris_dataset()
    x_train, x_test, y_train, y_test = train_test_split(iris_data, iris_target, test_size=0.25)
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(x_train, y_train)
    y_predict = knn.predict(x_test)
    # 预测结果展示
    labels = ['山鸢尾', '虹膜锦葵', '变色鸢尾']
    for i in range(len(y_predict)):
        print("第%d次测试：真实值：%s\t预测值：%s" % ((i+1), labels[y_predict[i]], labels[y_test[i]]))
    print('accuracy:', knn.score(x_test, y_test))


train_by_knn()