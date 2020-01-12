#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/1/11 16:33
"""
import pandas as pd

list_csv = ['data_1.csv', 'data_2.csv']
tmp = pd.read_csv(list_csv[0])
tmp.to_csv("all.csv", mode='w', index=False, header=True)
for i in list_csv[1:]:
    tmp = pd.read_csv(i)
    # append的方式加入到csv文件中
    tmp.to_csv("all.csv", mode='a', index=False, header=False)
tmp = pd.read_csv("all.csv")
# 删除重复的行
tmp = tmp.drop_duplicates()
# index为False代表没有保存列索引，header为True代表保存列名称
tmp.to_csv("all.csv", index=False, header=True)

