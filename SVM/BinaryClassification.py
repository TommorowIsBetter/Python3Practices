#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/6/5 15:26
"""
from sklearn import svm
# 基本数据
x = [[3, 1], [3, 9], [4, 9], [5, 2]]
# 结果分类
y = [1, -1, -1, 1]
# 分类模型，线性可分采用linear
model = svm.SVC(kernel='linear')
# 训练
model = model.fit(x, y)
# 打印支持向量的（点）
print(model.support_vectors_)
# 支持向量在数据集中的索引
print(model.support_)
# 新数据
new_one = [[3, 3]]
# 模型划分
print(model.predict(new_one))

