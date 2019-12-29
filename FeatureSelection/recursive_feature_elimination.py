#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/29 19:02
"""
from sklearn.datasets import load_boston
# 导入RFE方法和线性回归基模型
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

boston = load_boston()
X, y = boston.data, boston.target
print("全部特征：", boston.feature_names)
rfe = RFE(
    # 选择lin线性回归为基模型
    estimator=LinearRegression(),
    # 选区特征数
    n_features_to_select=7
)

# fit 方法训练选择特征属性
sFeature = rfe.fit_transform(X, y)
# 查看满足条件的属性
print("被选中的特征：", boston.feature_names[rfe.get_support()])
