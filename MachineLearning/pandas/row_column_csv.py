#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/5 10:45
"""
import pandas as pd
data = {'年龄': [12, 14, 10, 21, 22, 25, 25],
        '身高': [145, 160, 150, 160, 175, 180, 160],
        '性别': ['男', '女', '女', '女', '男', '男', '女']
        }
data_learn = pd.DataFrame(data)
# 查询数据
print(list(data_learn['年龄']))
list_address = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# 插入数据
data_learn.insert(len(data_learn.keys()), '住址', list_address)
# 删除列数据
data_learn = data_learn.drop(['性别'], axis=1)
print(data_learn)
