#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/10 21:40
"""
from matplotlib import pyplot as plt
import cv2
import numpy as np
np.set_printoptions(suppress=True)
img = cv2.imread('5.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img_gray, cmap=plt.cm.gray)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
print(type(hist))
# 计算所有像素点的和
print(np.sum(hist))
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
