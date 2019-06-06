#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/6/6 14:29
"""
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np
X, y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.6)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap="rainbow")
plt.xticks([])
plt.yticks([])
plt.show()
# 首先要有散点图
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap="rainbow")
# 获取当前的子图，如果不存在，则创建新的子图
ax = plt.gca()
xlim = ax.get_xlim()
# 默认创建(0.0,1.0)范围内的横纵坐标
ylim = ax.get_ylim()
# 要画决策边界，必须要有网格
axisx = np.linspace(xlim[0], xlim[1], 30)
axisy = np.linspace(ylim[0], ylim[1], 30)
axisy, axisx = np.meshgrid(axisy, axisx)
# 将特征向量转换为特征矩阵的函数
# 核心是将两个特征向量广播，以便获取y.shape * x.shape这么多个坐标点的横坐标和纵坐标
xy = np.vstack([axisx.ravel(), axisy.ravel()]).T
# 获取y.shape * x.shape这么多个坐标点
# 其中ravel()是降维函数，vstack能够将多个结构一致的一维数组按行堆叠起来c
# xy就是已经形成的网络，它是遍布在整个画布上的密集的点
# 建模，通过fit计算出对应的决策边界
clf = SVC(kernel="linear").fit(X, y)
p = clf.decision_function(xy).reshape(axisx.shape)
# 重要接口decision_function,返回每个输入的样本对应到决策边界的距离
# 然后将这个距离转换为axisx结构
# 画决策边界和平行于决策边界的超平面
ax.contour(axisx, axisy, p
           , colors="k"
           , levels=[-1, 0, 1]
           , alpha=0.5
           , linestyles=["--", "-", "--"])
ax.set_xlim(xlim)
ax.set_ylim(ylim)
plt.show()

