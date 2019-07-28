#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/7/19 20:52
"""
import os
dir = "./test_folder/"
print(len(os.listdir(dir)))


# 计算文件夹下及其子文件夹下的所有文件的个数
def count_file_number(dir):
    file_count = 0
    for dir_path, dir_names, file_names in os.walk(dir):
        for file in file_names:
            file_count = file_count + 1
    return file_count
print(count_file_number(dir))
