#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/11/30 12:13
"""
import pandas as pd
data = {'animal': ['cat', 'dog', 'cat', 'lion'],
        'foot': [2, 3, 5, 3],
        'scale': ['big', 'small', 'big', 'small']
        }
data_learn = pd.DataFrame(data)
print(data_learn)
# 完整特征编码
dummies = pd.get_dummies(data_learn, columns=data_learn.columns)
print(dummies)
list_one_hot = ['animal', 'scale']
for i in list_one_hot:
    # 特定特征编码
    dummies = pd.get_dummies(data_learn[i])
    dummies = dummies.add_prefix("{}_".format(i))
    data_learn.drop(i, axis=1, inplace=True)
    data_learn = data_learn.join(dummies)
print(data_learn)
# 把数据保存到csv文件中，保留标题栏，去除左边的下标
data_learn.to_csv('test.csv', index=False, header=True)
