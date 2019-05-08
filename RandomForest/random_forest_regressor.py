#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/8 19:26
"""
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
# 使数据不以科学计数法打印出来
np.set_printoptions(suppress=True)
# 加载数据
boston = load_boston()
# 分割训练数据和测试数据
x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.3, random_state=42)
# 对训练数据和测试数据进行标准化处理，x_train和x_test用一种参数标准化
ss_x = StandardScaler()
x_train = ss_x.fit_transform(x_train)
x_test = ss_x.transform(x_test)
ss_y = StandardScaler()
# 使label之变成一列
y_train = ss_y.fit_transform(y_train.reshape(-1, 1))
y_test = ss_y.transform(y_test.reshape(-1, 1))
# 随机森林回归
rfc = RandomForestRegressor()
# 训练
rfc.fit(x_train, y_train)
# 打印预测的值与实际的值
print rfc.predict(x_test), y_test
# 预测并返回预测精度
print rfc.score(x_test, y_test)


