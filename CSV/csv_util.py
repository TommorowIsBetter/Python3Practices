#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/9 16:41
"""
import csv
import pandas as pd

# 写入列表数据到csv文件中
def save_list_csv():
    data = [['name', 'age'],
            ['Bob', 14],
            ['Tom', 23],
            ['Jerry', '18']]
    with open('data_1.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

# 写入字典数据到csv文件中
def save_dic_csv():
    listStu = []
    data1 = {'name': 'WangYan', 'age': 18, 'Region': 'SuQian'}
    data2 = {'name': 'LeiLei', 'age': 19, 'Region': 'NanJing'}
    listStu.append(data1)
    listStu.append(data2)
    with open('data_1.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in listStu:
            writer.writerow(row.values())


# 一次性读取整个csv文件
def read_csv_all():
    with open('data_1.csv', 'r') as file_object:
        for line in file_object:
            # 调用rstrip()消除空白行
            print(line.rstrip())


# 逐行读取csv文件
def read_csv_line():
    with open('data_1.csv', 'r') as file_object:
        for line in file_object:
            # 调用rstrip()消除空白行
            print(line.rstrip())


# 创建一个包含各行内容的列表
def read_csv_line_list():
    with open('data_1.csv', 'r') as file_object:
        lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())


# 读取csv文件，用csv模块读取
def read_by_csv():
    with open('data_1.csv', 'r') as file_object:
        reader = csv.reader(file_object)
        for line in reader:
            print(line)


def get_app_name_by_picture_name(picture_number):
    # 根据图片名字找到所对应的APP应用名称
    data = pd.read_csv('ui_details.csv')
    index_number = data['UI Number'].tolist().index(picture_number)
    row_data = data.iloc[index_number]
    return row_data.tolist()[1]


if __name__ == '__main__':
    # save_dic_csv()
    print(get_app_name_by_picture_name(241))

