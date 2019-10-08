#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/10/7 18:13
"""
import cv2
import numpy as np

img = cv2.imread('lines.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
# 最低线段的长度，小于这个值的线段被抛弃
minLineLength = 100
# 线段中点与点之间连接起来的最大距离，在此范围内才被认为是单行
maxLineGap = 3
# 100阈值，累加平面的阈值参数，即：识别某部分为图中的一条直线时它在累加平面必须达到的值，低于此值的直线将被忽略。
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
for i in range(len(lines)):
    for x1, y1, x2, y2 in lines[i]:
        print(x1, y1, x2, y2)
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # 裁剪坐标为[y0:y1, x0:x1]
        cropped = img[y1 - 50:y1, x1:x2]
        cv2.imwrite(str(i) + ".jpg", cropped)
cv2.imshow("edges", edges)
cv2.imshow("lines", img)
cv2.waitKey()
cv2.destroyAllWindows()
