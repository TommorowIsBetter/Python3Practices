#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2021/1/8 21:53
"""
import cv2
import numpy as np

def crop_image(x_location, y_location, image):
    # 截取点击坐标出的图片
    # 截取点击坐标出的图片
    img_height, img_width = image.shape[:2]
    print(image.shape)
    img_size = img_width * img_height
    canny = cv2.Canny(image, 100, 150)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    for _ in range(3):
        canny = cv2.dilate(canny, kernel)
    # cv2.namedWindow("image1", 0)
    # cv2.imshow("image1", canny)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
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
    for x1, y1, w1, h1 in rect_list:
        # 找到包含点击位置的矩形
        if x1 <= x_location <= x1 + w1 and y1 <= y_location <= y1 + h1:
            cropped_image = image[y1:y1 + h1, x1:x1 + w1]
            return cropped_image, x1, y1, w1, h1
    return 0, 0, 0, 10, 10


if __name__ == '__main__':
    image_ = cv2.imread("pictures/pic6.png")
    crop_image_1, _, _, _, _ = crop_image(20, 40, image_)
    cv2.imshow("image", crop_image_1)
    cv2.waitKey()
    cv2.destroyAllWindows()
