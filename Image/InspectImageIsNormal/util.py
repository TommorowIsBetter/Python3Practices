#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/1/10 21:45
"""
import os
import cv2
def test_image(dir_):
    list_image = os.listdir(dir_)
    for i_ in list_image:
        # 读取和json匹配的图片
        try:
            image = cv2.imread(dir_ + i_)
            cv2.imshow("image", image)
        except:
            print(dir_ + i_)
            # 删除那些是有问题的图片，然后在把这些数据拿去解析
            os.remove(dir_ + i_)


if __name__ == '__main__':
    try:
        list_name = os.listdir('./ADBFILE')
    except Exception as e:
        print(e)
    for i in list_name:
        try:
            file_name_list = os.listdir('./ADBFILE' + '/' + i)
        except Exception as e:
            print(e)
            continue
        event_picture = './ADBFILE' + '/' + i + '/' + file_name_list[2] + '/'
        test_image(event_picture)
