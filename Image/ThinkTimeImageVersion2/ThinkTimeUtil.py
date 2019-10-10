#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/9/29 14:09
"""
import os
import time
import re
import shutil
import cv2

# 这里只需要把原始图片放到A_Pictures_Raw文件夹下即可，然后运行程序会把相应的处理后的图片放到New文件夹下
dir_New = "./A_Pictures_New/"
dir_raw = "./A_Pictures_Raw/"
# 为了实现把文件A_Pictures_Raw的图片重命名，命名要求是前一张图片的名字对应后一张的图片名字
# 注意这里enumerate的遍历顺序不是按照顺序，所以要确认命名的顺序正确。
def rename_picture_by_time_cv2():
    if not os.path.exists(dir_New):
        os.makedirs(dir_New)
    filename_list = os.listdir(dir_raw)
    listTime = []
    for i in range(len(filename_list) - 1):
        time1 = filename_list[i][0:14]
        timeArray1 = time.strptime(time1, '%Y%m%d%H%M%S')
        timeStamp1 = int(time.mktime(timeArray1))
        time2 = filename_list[i + 1][0:14]
        timeArray2 = time.strptime(time2, '%Y%m%d%H%M%S')
        timeStamp2 = int(time.mktime(timeArray2))
        listTime.append(timeStamp2 - timeStamp1)
    print(listTime)
    for index, file_name in enumerate(filename_list):
        print(index, file_name)
        if index < len(filename_list) - 1:
            img = cv2.imread(dir_raw + file_name)
            cv2.imwrite(dir_New + str(index) + '_' + str(listTime[index]) + '.png', img)
    filename_list_new = os.listdir(dir_New)
    print(filename_list_new)


rename_picture_by_time_cv2()
