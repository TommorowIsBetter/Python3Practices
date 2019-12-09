#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/11/30 12:59
"""
import pandas as pd
CSV_FILE_PATH = './ThinkTime.csv'
df = pd.read_csv(CSV_FILE_PATH)
print(df)

