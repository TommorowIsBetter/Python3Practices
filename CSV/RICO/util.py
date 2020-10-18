#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/10/17 16:58
"""
import pandas as pd
import json
import time
def get_app_name_by_picture_name(picture_number):
    # 根据图片名字找到所对应的APP应用名称
    data = pd.read_csv('ui_details.csv')
    index_number = data['UI Number'].tolist().index(picture_number)
    row_data = data.iloc[index_number]
    return row_data.tolist()[1]

finished_list = []
with open('result.json', 'r') as f:
    data = json.load(f)
    for i in data:
        finished_list.append(i)
        print(i)


with open('have_read.json', 'r') as f:
    data = json.load(f)
    for i in data:
        finished_list.append(i)
        print(i)

def get_category(package_name):
    from bs4 import BeautifulSoup
    import requests
    import sys
    import io
    # url = 'https://play.google.com/store/apps/details?id=com.doublerouble.counter'
    url = 'https://play.google.com/store/apps/details?id=' + package_name
    requests.DEFAULT_RETRIES = 5
    r = requests.get(url)
    s = requests.session()
    s.keep_alive = False
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
    # print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    if soup.find_all('a', class_='hrTbp R8zArc'):
        return soup.find_all('a', class_='hrTbp R8zArc')[1].get_text()
    else:
        return 'null'


print(finished_list)
finished_list = [i.split('.')[0] for i in finished_list]
dic_package = {}
with open('ui_details.csv', 'r') as file_object:
    lines = file_object.readlines()
for line in lines[1:]:
    number, package_name = line.rstrip().split(',')[0], line.rstrip().split(',')[1]
    dic_package[number] = package_name
category_list = {}

with open('data.json', 'r') as f:
    category_list = json.load(f)
    pre_finished_list = category_list.keys()

for i in finished_list:
    if i in dic_package and i not in pre_finished_list:
        print(dic_package[i])
        category_list[i] = get_category(dic_package[i])
        time.sleep(5)
        data = category_list
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

# import urllib.request
#
# url = "https://play.google.com/store/apps/details?id=com.doublerouble.counter"
# response = urllib.request.urlopen(url)
# content = response.read().decode('utf-8')
# print(content.encode('utf-8'))

