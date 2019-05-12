#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/9 16:41
"""
import csv


# 写入数据到csv文件中
def save_csv():
    data = [['name', 'age'],
            ['Bob', 14],
            ['Tom', 23],
            ['Jerry', '18']]
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


# 一次性读取整个csv文件
def read_csv_all():
    with open('data.csv', 'r') as file_object:
        for line in file_object:
            # 调用rstrip()消除空白行
            print(line.rstrip())


# 逐行读取csv文件
def read_csv_line():
    with open('data.csv', 'r') as file_object:
        for line in file_object:
            # 调用rstrip()消除空白行
            print(line.rstrip())


# 创建一个包含各行内容的列表
def read_csv_line_list():
    with open('data.csv', 'r') as file_object:
        lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())


read_csv_all()

