#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/10/8 20:26
"""
import base64
import json
# 防止https证书校验不正确
import ssl
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request
from urllib.request import urlopen

import cv2
import numpy

ssl._create_default_https_context = ssl._create_unverified_context
API_KEY = 's13NO7yPOIdwRQnt9r3MswSc'
SECRET_KEY = 'xUzLHmkfAXMRGGOAe9FG7vG2ULNmzQbm'
OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'

def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)
    result_str = result_str.decode()
    result_ = json.loads(result_str)
    if 'access_token' in result_.keys() and 'scope' in result_.keys():
        if not 'brain_all_scope' in result_['scope'].split(' '):
            print('please ensure has checked the ability')
            exit()
        return result_['access_token']
    else:
        print('please overwrite the correct API_KEY and SECRET_KEY')
        exit()


def read_file(image_path):
    f = None
    try:
        f = open(image_path, 'rb')
        return f.read()
    except:
        print('read image file fail')
        return None
    finally:
        if f:
            f.close()


def request(url, data):
    req = Request(url, data.encode('utf-8'))
    try:
        f = urlopen(req)
        result_str = f.read()
        result_str = result_str.decode()
        return result_str
    except URLError as err:
        print(err)

def get_text_by_ocr(image_):
    # 根据cv2.imread()读取到的图片进行文字OCR识别
    # 获取access token
    token = fetch_token()
    # 拼接通用文字识别高精度url
    image_url = OCR_URL + "?access_token=" + token
    text = ""
    image = cv2.imencode('.png', image_)[1]
    result = request(image_url, urlencode({'image': base64.b64encode(image)}))
    # 解析返回结果
    result_json = json.loads(result)
    for words_result in result_json["words_result"]:
        text = text + words_result["words"]
    # 打印文字
    print(text)
if __name__ == '__main__':
    img = cv2.imread('d.png')
    thresh = cv2.Canny(img, 40, 70)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, numpy.ones((5, 5), numpy.uint8))
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    del_index = []
    new_list = []
    for i, count in zip(contours, range(len(contours))):
        if cv2.contourArea(i) < img.size * 0.004:
            del_index.append(count)
    for i in range(len(contours)):
        if i not in del_index:
            new_list.append(contours[i])
    lines_list = new_list
    for i in range(0, len(lines_list)):
        cn = lines_list[i]
        x, y, w, h = cv2.boundingRect(cn)
        region = img[y:y+h, x:x+w]
        cv2.imshow("region", region)
        get_text_by_ocr(region)
        draw_0 = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3, 4, 0)
    cv2.namedWindow('draw_0', 0)
    cv2.imshow("draw_0", draw_0)
    cv2.waitKey(0)
    cv2.destroyWindow("draw_0")