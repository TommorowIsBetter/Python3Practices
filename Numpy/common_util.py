#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/7 16:47
"""
import numpy as np
num1 = np.array([[2, 2], [3, 5]])
# axis 不设置值，对 m*n 个数求均值，返回一个实数
print np.mean(num1)
# axis = 0：压缩行，对各列求均值，返回 1* n 矩阵
print np.mean(num1, 0)
# axis =1 ：压缩列，对各行求均值，返回 m *1 矩阵
print np.mean(num1, 1)



