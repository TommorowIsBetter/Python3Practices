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
           '&client_id=D7Sfn62R1VAZkZKHhFDV0TkS&client_secret=1b99SoateGeAG5GE9XGDAW9CEjuditIg'
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
        "text": "我希望我可以完美的过完这一生。"
    })
    print(d)
    # noinspection PyBroadException
    try:
        print("start ...")
        r = requests.post(
            'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?'
            'access_token=24.201ee75150221061594597cf25a3cec0.2592000.1566980927.282335-16240166', data=d)
        res = json.loads(r.text)
        allemotion = res['items'][0]['sentiment']
        print(allemotion)
        print("end ...")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 进行情感倾向分析
    emotion_analysis()
