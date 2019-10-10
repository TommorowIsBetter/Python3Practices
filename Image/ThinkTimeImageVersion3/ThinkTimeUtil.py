#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/10/10 15:02
@Description: 1. 这里是根据图片的大小判断获取到的图片是否是同一张图片，因为采集的图片有可能用户看的是一张图片，而系统后台
采集了多张。造成这种原因是因为手机界面改变，而用户察觉不到，但是系统后台可以察觉到的。如果连续的几张图片大小相差不超过1，
则表示为同一张照片，删除其它的多余照片。2. 删除多余图片后，接着可以对每张图片计算相应的停留时间
"""
import os
import cv2
import time
# 这里只需要把原始图片放到A_Pictures_Raw文件夹下即可，然后运行程序会把相应的处理后的图片放到New文件夹下
dir_New = "./A_Pictures_New/"
dir_Temp = "./A_Pictures_Temp/"
dir_Raw = "./A_Pictures_Raw/"
def del_repeat_image_by_size():
    if not os.path.exists(dir_Temp):
        os.makedirs(dir_Temp)
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
            cv2.imwrite(dir_Temp + file_name, img)

def rename_picture_by_time_cv2():
    if not os.path.exists(dir_New):
        os.makedirs(dir_New)
    filename_list = os.listdir(dir_Temp)
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
            img = cv2.imread(dir_Temp + file_name)
            cv2.imwrite(dir_New + str(index) + '_' + str(listTime[index]) + '.png', img)
    filename_list_new = os.listdir(dir_New)
    print(filename_list_new)


if __name__ == '__main__':
    # 根据图片大小来删除多余的照片
    del_repeat_image_by_size()
    # 确定每张照片对应的停留时间
    rename_picture_by_time_cv2()
