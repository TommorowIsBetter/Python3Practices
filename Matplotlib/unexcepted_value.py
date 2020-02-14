#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/2/14 17:22
@description:对每个样本的选定特征值进行异常值检测
"""
# Outlier detection
import pandas as pd
import numpy as np
from collections import Counter


def detect_outliers(df, n, features):
    """
    :param df:
    :param n: 每个样本的异常值个数不能超过n个
    :param features:
    :return:
    """
    outlier_indices = []
    # iterate over features(columns)
    for col in features:
        # 1st quartile (25%)
        Q1 = np.percentile(df[col], 25)
        # 3rd quartile (75%)
        Q3 = np.percentile(df[col], 75)
        # Inter quartile range (IQR)
        IQR = Q3 - Q1
        # outlier step
        outlier_step = 1.5 * IQR
        # Determine a list of indices of outliers for feature col
        outlier_list_col = df[(df[col] < Q1 - outlier_step) | (df[col] > Q3 + outlier_step)].index
        # append the found outlier indices for col to the list of outlier indices
        outlier_indices.extend(outlier_list_col)
    # select observations containing more than 2 outliers
    outlier_indices = Counter(outlier_indices)
    multiple_outliers = list(k for k, v in outlier_indices.items() if v > n)
    return multiple_outliers


# detect outliers from "Col1","Col2","Col3","Col4"
df = pd.read_csv("data.csv")
Outliers_to_drop = detect_outliers(df,2,["Col1","Col2","Col3","Col4"])
# Drop outliers
df = df.drop(Outliers_to_drop, axis = 0).reset_index(drop=True)