#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/7/27 20:23
"""

import os
import cv2
# 为了实现把文件A_Pictures_Raw的图片重命名，命名要求是前一张图片的名字对应后一张的图片名字
name_list = os.listdir("./A_Pictures_Raw")
for i, filename in enumerate(name_list):
    if i < len(name_list) - 1:
        img = cv2.imread("./A_Pictures_Raw/" + filename)
        cv2.imwrite("./A_Pictures_New/" + name_list[i + 1], img)
