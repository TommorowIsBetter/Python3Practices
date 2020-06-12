#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/6/11 14:35
"""
import cv2
import base64
import json
import requests
url = 'http://192.168.1.102:8089/api/tr-run/'

image = cv2.imread('a.png')
cv_encoded_image = cv2.imencode('.png', image)[1]
base64image = base64.b64encode(cv_encoded_image).decode("utf-8")
data = {'img': base64image, 'compress': 0}
res = requests.post(url=url, data=data)
print(res.content)