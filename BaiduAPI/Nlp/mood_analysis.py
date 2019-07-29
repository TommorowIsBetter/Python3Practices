#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/13 19:06
"""


import urllib.request
import requests
import json
import io


def get_access_token():
    """
    用于根据client_id和client_secret获取access_token
    """
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
           '&client_id=B2KyKzMH1K3SX2WCwbMoNVXu&client_secret=dUpm2eKghoubZVR6UKDmRafKww20cFHz'
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    if content:
        print(content)


def mood_analysis():
    """
    情感分析
    """
    d = json.dumps({
        "text": "菜鸡，别在送人头了！"
    })
    # noinspection PyBroadException
    try:
        print("start ...")
        r = requests.post(
            'https://aip.baidubce.com/rpc/2.0/nlp/v1/emotion?'
            'access_token=24.201ee75150221061594597cf25a3cec0.2592000.1566980927.282335-16240166', data=d)
        res = json.loads(r.text)
        print(res['items'][0]['replies'][0])
        print("end ...")
    except Exception as e:
        pass


if __name__ == '__main__':
    # 对话情绪识别
    mood_analysis()
