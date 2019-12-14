#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/13 19:25
"""
import json
import math

import cv2
import numpy as np


def cal_image_entropy(image):
    # 获取图片信息熵的功能
    # 首先初始化图片信息熵的值
    image_entropy = 0
    tmp = [0] * 256
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


def cal_average_gray(img):
    # 计算图片的灰度平均值功能
    height, width = img.shape
    size = img.size
    average = 0
    for i in range(height):
        for j in range(width):
            average += img[i][j] / size
    return average

def cal_contrast(img):
    # 计算图片的对比度
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


def rectangle_and_get_information(json_file_, picture_file_):
    # 获取局部图片的特征信息，json_file_为json的路径，picture_file_为picture的路径
    # 色调值初始值
    h_value = 0
    # 饱和度初始值
    s_value = 0
    # 明度值初始值
    v_value = 0
    # 图片信息熵初始值
    image_entropy = 0
    # 图片灰度平均值初始化
    image_average = 0
    # 图片对比度初始化
    image_contrast = 0
    # 读取图片
    image = cv2.imread(picture_file_)
    with open(json_file_, 'rb+') as data_file:
        content = json.load(data_file)
        nodes = content['nodes']
        for node in nodes:
            if 0 < node['inScreenBounds']['bottom'] < 1184 and 0 < node['inScreenBounds']['top'] < 1184 and \
                    0 < node['inScreenBounds']['left'] < 720 and 0 < node['inScreenBounds']['right'] < 720:
                #  这个主要用于在原图中显示已经被选中的矩形框
                #  (left, top),(right,bottom) 按照这个顺序，具体的数值通过在json文件里面进行获取
                draw_0 = cv2.rectangle(image, (node['inScreenBounds']['left'], node['inScreenBounds']['top']),
                                       (node['inScreenBounds']['right'], node['inScreenBounds']['bottom']),
                                       (0, 0, 255), 3, 4, 0)
                # 对选中的局部图片进行分析 [top:bottom, left:right]按照这个顺序进行放置
                region = image[node['inScreenBounds']['top']:node['inScreenBounds']['bottom'],
                               node['inScreenBounds']['left']:node['inScreenBounds']['right']]
                h_s_v = cv2.cvtColor(region, cv2.COLOR_BGR2HSV)
                h, s, v = cv2.split(h_s_v)
                # 1.获取色调值
                h_value += round(np.sum(h), 2)
                # 2.获取饱和度值
                s_value += round(np.sum(s), 2)
                # 3.获取明度值
                v_value += round(np.sum(v), 2)
                # 把彩色图片转为灰度图片
                region = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
                # 4.获取图片信息熵
                image_entropy += cal_image_entropy(region)
                # 5.获取图片灰度值平均值
                image_average += cal_average_gray(region)
                # 6.获取图片的对比度
                image_contrast += cal_contrast(region)
    print(round(h_value, 2), round(s_value, 2), round(v_value), image_entropy, image_average, image_contrast)
    # 显示画过矩形框的图片
    cv2.namedWindow('draw_0', 0)
    cv2.imshow("draw_0", draw_0)
    cv2.waitKey(0)
    cv2.destroyWindow("draw_0")

if __name__ == '__main__':
    json_file = 'F:\\CommonFiles\\PyCharmProject\\Python3Practices\\Image\Rectangle\\20191213171916715.json'
    picture_file = 'F:\\CommonFiles\\PyCharmProject\\Python3Practices\\Image\Rectangle\\20191213171916715.png'
    rectangle_and_get_information(json_file, picture_file)
