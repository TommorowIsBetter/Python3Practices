#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/3/27 9:45
"""

import urllib.request
import requests
import json


def get_access_token():
    """
    用于根据client_id和client_secret获取access_token
    """
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
           '&client_id=B5WOK51SVGddGBe8sW1aAZms&client_secret=UGwbR2z4ykpFEL4a9Wme7MujTmbNoVpM'
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        print(content)


def emotion_analysis():
    """
    情感分析
    """
    d = json.dumps({
        "text": "百度是一家高科技公司"
    })
    print(d)
    # noinspection PyBroadException
    try:
        print("start ...")
        r = requests.post(
            'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?'
            'access_token=24.904e72e2b69e2400864065541a8dd264.2592000.1556244820.282335-15858257', data=d)
        res = json.loads(r.text)
        allemotion = res['items'][0]['sentiment']
        print(allemotion)
        print("end ...")
    except Exception as e:
        pass


# 获取access_token
get_access_token()
# 进行情感值分析
emotion_analysis()
