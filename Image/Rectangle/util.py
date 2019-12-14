#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/14 12:23
"""
import math

import cv2
import numpy as np
def cal_image_entropy(image_file_):
    # 计算图片的信息熵
    # 初始化图片信息熵的值
    image_entropy = 0
    tmp = [0] * 256
    image = cv2.imread(image_file_, 0)
    image_size = image.size
    image = np.array(image)
    for i in range(len(image)):
        for j in range(len(image[i])):
            val = image[i][j]
            tmp[val] = tmp[val] + 1
    for i in range(len(tmp)):
        tmp[i] = tmp[i] / image_size
    for i in range(len(tmp)):
        if tmp[i] != 0:
            image_entropy = image_entropy - tmp[i] * (math.log(tmp[i]) / math.log(2))
    return image_entropy


def cal_average_gray(image_file_):
    # 计算图片的灰度平均值
    img = cv2.imread(image_file_, 0)
    height, width = img.shape
    size = img.size
    average = 0
    for i in range(height):
        for j in range(width):
            average += img[i][j] / size
    return average


def cal_contrast(image_file_):
    # 计算图片的对比度
    img = cv2.imread(image_file_)
    # 计算图片的对比度
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = img.shape
    # 图片矩阵向外扩展一个像素
    img_ext = cv2.copyMakeBorder(img, 1, 1, 1, 1, cv2.BORDER_REPLICATE)
    rows_ext, cols_ext = img_ext.shape
    square_sum = 0.0
    for i in range(1, rows_ext - 1):
        for j in range(1, cols_ext - 1):
            square_sum += ((int(img_ext[i, j]) - int(img_ext[i, j + 1])) ** 2 + (int(img_ext[i, j]) -
                            int(img_ext[i, j - 1])) ** 2 + (int(img_ext[i, j]) - int(img_ext[i + 1, j])) ** 2 +
                           (int(img_ext[i, j]) - int(img_ext[i - 1, j])) ** 2)
    image_contrast = square_sum / (4 * (height - 2) * (width - 2) + 3 * (2 * (height - 2) + 2 * (width - 2)) + 2 * 4)
    return image_contrast

def cal_hsv(image_file_):
    # 计算图片的HSV
    img = cv2.imread(image_file_)
    h_s_v = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(h_s_v)
    # 获取色调值, 饱和度值, 明度值
    return round(np.sum(h), 2), round(np.sum(s), 2), round(np.sum(v), 2)


if __name__ == '__main__':
    image_file = '20191213171916715.png'
    print(cal_image_entropy(image_file))
    print(cal_average_gray(image_file))
    print(cal_contrast(image_file))
    print(cal_hsv(image_file))
