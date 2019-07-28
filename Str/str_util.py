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


# 第二个参数为 1，返回两个参数列表
str_name = "Google#Runoob#Taobao#Facebook"
name = str_name.split("#", 2)
print(name)
