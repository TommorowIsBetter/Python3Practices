#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/10/18 16:13
"""
from collections import Counter
import json
import matplotlib.pyplot as plt

with open('data.json', 'r') as f:
    data = json.load(f)
app_list = data.values()
print(list(app_list))
print(dict(Counter(list(app_list))))

x = [1, 2, 3, 4, 5]
y = [5, 7, 4, 3, 1]
x_label = ['pop', 'classic', 'pure', 'blue', 'electronic']

x = list(range(len(dict(Counter(list(app_list)))) + 1)[1:])
y = list(dict(Counter(list(app_list))).values())
x_label = list(dict(Counter(list(app_list))).keys())
plt.xticks(x, x_label, rotation=80)
plt.bar(x, y)
plt.show()


