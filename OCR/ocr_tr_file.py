#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/6/12 12:55
"""
import requests

url3 = 'http://192.168.1.102:8089/api/tr-run/'
files = {'file': open('0.png', 'rb')}
data = {'compress': 1600}
response = requests.post(url=url3, files=files, data=data)
json = response.json()
print(json['data']['raw_out'])
