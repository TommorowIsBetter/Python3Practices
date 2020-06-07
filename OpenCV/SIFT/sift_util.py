#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/6/7 19:58
"""
import cv2


def cal_similarity(image1, image2):
    # 实例化
    sift = cv2.xfeatures2d.SIFT_create()
    # 计算关键点和描述子,其中kp为关键点keypoints,des为描述子descriptors
    kp1, des1 = sift.detectAndCompute(image1, None)
    kp2, des2 = sift.detectAndCompute(image2, None)
    # 参数设计和实例化
    index_params = dict(algorithm=1, trees=6)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    # 利用knn计算两个描述子的匹配
    matche = flann.knnMatch(des1, des2, k=2)
    # 绘出匹配效果
    result = []
    for m, n in matche:
        if m.distance < 0.6 * n.distance:
            result.append(m)
    if len(result) > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    img1 = cv2.imread('333.png')
    img2 = cv2.imread('search.png')
    print(cal_similarity(img1, img2))