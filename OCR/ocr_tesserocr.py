#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/11/18 20:13
"""
from PIL import Image
import tesserocr
image = Image.open('id_card.png')
print(tesserocr.image_to_text(image, lang='chi_sim'))
