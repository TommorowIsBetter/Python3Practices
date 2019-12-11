#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/11 14:47
"""
import cv2
import numpy as np
image = cv2.imread('20191202200047138.png')
HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(HSV)
print(np.mean(H))
print(np.mean(S))
print(np.mean(V))
