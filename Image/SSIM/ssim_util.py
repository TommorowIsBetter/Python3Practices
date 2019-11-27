#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/11/27 11:18
"""
import cv2
import numpy as np
import copy
from matplotlib import pyplot as plt
from skimage.measure import compare_ssim
from PIL import Image
# im = Image.open('a.png')
# out = im.resize((378, 514), Image.ANTIALIAS)
# out.save('a.png')
image_1 = cv2.imread('a.png')
image_2 = cv2.imread('b.png')
cv2.imshow('pic_1', image_1)
cv2.imshow('pic_2', image_2)
gray_image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
cv2.imshow('pic_gray_1', gray_image_1)
gray_image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)
cv2.imshow('pic_gray_2', gray_image_2)
cv2.waitKey()
similarity, delta = compare_ssim(gray_image_1, gray_image_2, full=True)
print(similarity)

