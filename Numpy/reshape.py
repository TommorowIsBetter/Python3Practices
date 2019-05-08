#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/8 20:59
"""

import numpy as np
z = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(z.shape)
# 变成一列
print(z.reshape(-1, 1))
# 变成一行
print(z.reshape(1, -1))
# 变成两列
print(z.reshape(-1, 2))
# 变成两行
print(z.reshape(2, -1))

