#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/6 10:22
"""
import matplotlib.pyplot as plt
import pandas as pd

# 使用自带的样式进行美化
plt.style.use('ggplot')
# 用来正常显示负数
plt.rcParams['axes.unicode_minus'] = False
# 用来正常显示中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 创建一个空的DataFrame
df = pd.DataFrame()
# 添加成绩单，最后显示成绩单表格
df['英语'] = [76, -90, 97, 71, 70, 93, 86, 83, 78, 85, 81]
df['经济数学'] = [65, 95, 51, 74, 78, 63, 91, 82, 75, 71, 55]
df['西方经济学'] = [93, 81, 76, 88, 66, 79, 83, 92, 78, 86, 78]
df['计算机应用基础'] = [85, 78, 81, 95, 70, 67, 82, 72, 80, 81, 77]
print(df)
plt.boxplot(x=df.values, labels=df.columns, whis=1.5)
plt.show()
