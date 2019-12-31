#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/31 14:55
"""
from sklearn.datasets import load_boston
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor

boston = load_boston()
X, y = boston.data, boston.target
print("全部特征：", boston.feature_names)
rfe = RFE(
    # 选择随机森林为基模型
    estimator=RandomForestRegressor(n_estimators=20, max_depth=4),
    # 选区特征数
    n_features_to_select=7
)

# fit 方法训练选择特征属性
sFeature = rfe.fit_transform(X, y)
# 查看满足条件的属性
print("被选中的特征：", boston.feature_names[rfe.get_support()])
