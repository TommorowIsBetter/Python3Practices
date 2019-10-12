#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/10/12 16:05
"""
import os
import cv2
import uuid
dir_New = "./NewPictures/"
dir_Raw = "./RawPictures/"
char_ = '4'
def rename_image():
    if not os.path.exists(dir_New):
        os.makedirs(dir_New)
    fileName_list = os.listdir(dir_Raw)
    for index, nameImage in enumerate(fileName_list):
        img = cv2.imread(dir_Raw + nameImage)
        cv2.imwrite(dir_New + str(uuid.uuid1()).split('-')[0] + '_' + str(index) + '_' + char_ + '.png', img)

if __name__ == '__main__':
    rename_image()
