#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/10 21:49
"""
from matplotlib import pyplot as plt
import cv2
import numpy as np
np.set_printoptions(suppress=True)
img = cv2.imread('5.png')
chanel_s = cv2.split(img)
colors = ('r', 'b', 'g')
plt.figure()
plt.title("’Flattened’ Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chanel_s, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    print(np.sum(hist))
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
plt.show()
