#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2021/1/8 21:26
"""
import cv2


def mouse_event(event, x, y, flags, param):
    global rect_list
    global img
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.destroyWindow("widget")
        for x1, y1, w1, h1 in rect_list:
            # 找到包含点击位置的矩形
            if x1 <= x <= x1 + w1 and y1 <= y <= y1 + h1:
                cropped = img[y1:y1 + h1, x1:x1 + w1]
                cv2.imshow("widget", cropped)
                break


cv2.namedWindow("rect", 0)
cv2.resizeWindow("rect", 500, 800)
cv2.setMouseCallback('rect', mouse_event)
# 读取图片
img = cv2.imread("pictures/pic6.png")
img_height, img_width = img.shape[:2]
img_size = img_width * img_height

canny = cv2.Canny(img, 100, 150)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
for _ in range(3):
    canny = cv2.dilate(canny, kernel)
cv2.imwrite("Canny.jpg", canny)

_, contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

rect_list = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    # 排除面积过大的矩形框
    if w * h > img_size * 0.16:
        continue
    rect_list.append((x, y, w, h))
    # 将矩形框按面积大小排序
    rect_list.sort(key=lambda rect: rect[2] * rect[3], reverse=False)
cv2.imshow("rect", img)
cv2.waitKey(0)
