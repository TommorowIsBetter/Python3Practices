#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/10/7 18:13
"""
import cv2
import os
import numpy as np


def nothing():
    pass


# 设置展示图像的窗口大小
cv2.namedWindow("canny", 0)
cv2.resizeWindow("canny", 400, 800)

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
cv2.createTrackbar('pic_index', 'rect', 0, n - 1, nothing)
cv2.createTrackbar('minLineLength', 'rect', 0, 1000, nothing)
cv2.createTrackbar('maxLineGap', 'rect', 0, 100, nothing)

while True:
    i = cv2.getTrackbarPos('pic_index', 'rect')
    img = img_list[i]
    img_height, img_width = img.shape[:2]
    img_size = img_width * img_height

    img1 = img
    # 对中值滤波后的图像做canny运算，得到二值图
    canny_min = cv2.getTrackbarPos('canny_min', 'canny')
    canny_max = cv2.getTrackbarPos('canny_max', 'canny')
    canny = cv2.Canny(img1, canny_min, canny_max)
    cv2.imshow('canny', canny)
    min_line = cv2.getTrackbarPos('minLineLength', 'rect')
    max_gap = cv2.getTrackbarPos('maxLineGap', 'rect')
    lines = cv2.HoughLinesP(image=canny, rho=1, theta=np.pi / 180, threshold=100, minLineLength=min_line, maxLineGap=max_gap)
    img2 = img.copy()
    if lines is not None:
        for i in range(len(lines)):
            print(lines[i])
            for x1, y1, x2, y2 in lines[i]:
                cv2.line(img2, (x1, y1), (x2, y2), (255, 0, 0), 5)
    cv2.imshow("rect", img2)
    cv2.waitKey(30)
