#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/6/25 20:01
"""

import cv2
import os

def nothing():
    pass


# 设置展示图像的窗口大小
cv2.namedWindow("canny", 0)
cv2.resizeWindow("canny", 400, 800)

cv2.namedWindow("closed", 0)
cv2.resizeWindow("closed", 400, 800)

cv2.namedWindow("rect", 0)
cv2.resizeWindow("rect", 400, 800)

# 将测试用的图片读入内存，放在数组中
file_list = os.listdir('pictures')
n = len(file_list)
img_list = []
for i in range(n):
    pic_path = "pictures/" + file_list[i]
    img = cv2.imread(pic_path)
    img_list.append(img)

# 设置canny参数初始值
canny_min = 60
canny_max = 130

# 创建滚动条
cv2.createTrackbar('canny_min', 'canny', canny_min, 255, nothing)
cv2.createTrackbar('canny_max', 'canny', canny_max, 255, nothing)
cv2.createTrackbar('min_scale', 'rect', 0, 1000, nothing)
cv2.createTrackbar('max_scale', 'rect', 35, 1000, nothing)
cv2.createTrackbar('height', 'rect', 35, 200, nothing)
cv2.createTrackbar('pic_index', 'rect', 0, n - 1, nothing)

while True:
    i = cv2.getTrackbarPos('pic_index', 'rect')
    img = img_list[i]
    img_height, img_width = img.shape[:2]
    img_size = img_width * img_height

    img2 = img

    # 对中值滤波后的图像做canny运算，得到二值图
    canny_min = cv2.getTrackbarPos('canny_min', 'canny')
    canny_max = cv2.getTrackbarPos('canny_max', 'canny')
    canny = cv2.Canny(img2, canny_min, canny_max)
    cv2.imshow('canny', canny)

    # 对canny运算后的二值图做闭运算
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    closed = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('closed', closed)

    # 从闭运算后的二值图中提取轮廓
    _, contours, hierarchy = cv2.findContours(closed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 获得所有轮廓的外框图，并根据设置的控件大小阈值，对外框图进行筛选
    min_scale = cv2.getTrackbarPos('min_scale', 'rect') / 1000
    max_scale = cv2.getTrackbarPos('max_scale', 'rect') / 1000
    height = cv2.getTrackbarPos('height', 'rect')
    rect_list = []
    for j in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[j])
        if w * h < img_size * min_scale or w * h > img_size * max_scale or h < height:
            continue
        rect_list.append((x, y, w, h))    # 将筛选得到的外框图在原始图像上绘出
    img3 = img.copy()
    for x, y, w, h in rect_list:
        cv2.rectangle(img3, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("rect", img3)
    cv2.waitKey(30)