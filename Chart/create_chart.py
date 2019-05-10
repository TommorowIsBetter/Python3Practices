#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/10 21:10
"""
from pyecharts import Page, Bar


# 生成相应的图表
def generate_chart():
        """
        两个应用作为一个单位进行测试
        """
        page = Page()
        attr = ['网易云阅读 任阅', '天涯论坛 新奇日报', '知乎 知乎日报', '天猫 新浪微博', '豆瓣 亚马逊']
        v1 = [2.25, 2.33, 2.28, 2.13, 2.39]
        v2 = [1.48, 1.32, 1.79, 1.24, 1.27]
        bar1 = Bar("柱状图示例")
        bar1.add("实验一", attr, v1, xaxis_interval=0, xaxis_rotate=30)
        bar1.add("实验二", attr, v2, xaxis_interval=0, xaxis_rotate=30)
        page.add(bar1)

        attr = ['网易云阅读', '任阅', '天涯论坛', '新奇日报', '知乎', '知乎日报', '天猫',  '新浪微博', '豆瓣',  '亚马逊']
        v1 = [1.91, 2.53, 2.00, 2.20, 2.48, 1.77, 2.02, 2.21, 2.15, 1.71]
        v2 = [1.29, 1.60, 1.40, 1.32, 1.69, 1.64, 1.05, 1.37, 1.45, 1.55]
        bar2 = Bar("柱状图示例")
        bar2.add("实验一", attr, v1, xaxis_interval=0, xaxis_rotate=30)
        bar2.add("实验二", attr, v2, xaxis_interval=0, xaxis_rotate=30)
        page.add(bar2)
        page.render('chart.html')


if __name__ == '__main__':
        generate_chart()
