#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/6/11 13:08
"""
from PIL import Image
import pytesseract
image = Image.open('a.png')  # 打开图片
result = pytesseract.image_to_string(image, lang='chi_sim')  # 使用简体中文字库识别图片并返回结果
print(result)  # 打印识别的图片内容
