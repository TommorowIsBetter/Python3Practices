#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/9 16:41
"""
import csv
data = [['name', 'age'],
        ['Bob', 14],
        ['Tom', 23],
        ['Jerry', '18']]
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
