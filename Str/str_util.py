#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/7/10 16:39
"""
# 获取路径的文件名字
path = "K:/Project/FilterDriver/DriverCodes/hello.txt"
print(path.split("/")[-1].split(".")[0])
