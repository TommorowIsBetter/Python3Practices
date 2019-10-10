#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/10/10 15:02
@Description: 这里是根据图片的大小判断获取到的图片是否是同一张图片，因为采集的图片有可能用户看的是一张图片，而系统后台
采集了多张。造成这种原因是因为手机界面改变，而用户察觉不到，但是系统后台可以察觉到的。如果连续的几张图片大小相差不超过1，
则表示为同一张照片，删除其它的多余照片。
"""
import os
import cv2
# 这里只需要把原始图片放到A_Pictures_Raw文件夹下即可，然后运行程序会把相应的处理后的图片放到New文件夹下
dir_New = "./A_Pictures_New/"
dir_Raw = "./A_Pictures_Raw/"
fileName_list = os.listdir(dir_Raw)
fileSize_list = []
for nameImage in fileName_list:
    file_size = round(os.path.getsize(dir_Raw + nameImage)/1024)
    fileSize_list.append(file_size)
del_list = []
for i in range(len(fileSize_list)):
    for j in range(len(fileSize_list))[i + 1:]:
        if abs(fileSize_list[i]-fileSize_list[j]) <= 1:
            del_list.append(j)
        else:
            break
del_list = list(set(del_list))
newFileName_list = []
for i in range(len(fileName_list)):
    if i not in del_list:
        newFileName_list.append(fileName_list[i])
fileName_list = newFileName_list
for index, file_name in enumerate(fileName_list):
    print(index, file_name)
    if index < len(fileName_list):
        img = cv2.imread(dir_Raw + file_name)
        cv2.imwrite(dir_New + file_name, img)
