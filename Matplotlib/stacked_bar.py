#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/3/5 13:09
"""
import numpy as np
import matplotlib.pyplot as plt


labels = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6']
men_means = [20, 35, 30, 35, 27, 28]
women_means = [25, 32, 34, 20, 25, 10]
children_means = [12, 3, 13, 9, 9, 1]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()
d = []
for i in range(0, len(men_means)):
    sum = men_means[i] + women_means[i]
    d.append(sum)

ax.bar(labels, men_means, width, label='Men')
ax.bar(labels, women_means, width, bottom=men_means,
       label='Women')
ax.bar(labels, children_means, width, bottom=d,
       label='Children')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()
plt.show()
