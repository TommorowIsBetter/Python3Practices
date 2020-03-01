#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/3/1 12:05
"""
import matplotlib.pyplot as plt

fig, axes = plt.subplots()

# generate some random test data
all_data = [76, 90, 97, 71, 170, 93, 86, 83, 78, 85, 81]

# plot violin plot
axes.violinplot(all_data,
                showmeans=False,
                showmedians=True)
axes.set_title('Violin plot')

axes.yaxis.grid(True)
axes.set_xlabel('Four separate samples')
axes.set_ylabel('Observed values')

# add x-tick labels
plt.setp(axes, xticklabels=['x1'])
plt.show()
