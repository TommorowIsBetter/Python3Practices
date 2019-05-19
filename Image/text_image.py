#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/19 16:14
"""
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# 设置字体，如果没有，也可以不设置
font = ImageFont.truetype("demo.ttf", 50)

# 打开底版图片
imageFile = "./img/1.jpg"
im1 = Image.open(imageFile)

# 在图片上添加文字
draw = ImageDraw.Draw(im1)
draw.text((0, 0), "hello world", (255, 255, 0), font=font)
draw = ImageDraw.Draw(im1)
# 保存
im1.save("./out/target.png")
