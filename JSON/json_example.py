#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/3/27 15:51
"""

import json


def demo_loads():
    """
    把json格式数据转化为字典数据

    """
    data = '{"str3": "乔峰", "str2": "段誉", "str1": "John"}'
    d1 = json.loads(data)
    print(d1)
    print(d1['str2'])


def demo_dumps():
    """
    把字典数据转换为json类型数据

    """
    data = {'str3': 'liming', 'str2': 'xiaohong', 'str1': 'lilei'}
    # sort_keys是加入排序的意思
    d1 = json.dumps(data, sort_keys=True)
    d2 = json.dumps(data)
    # indent缩进的意思，使得json看起来更加整齐
    d3 = json.dumps(data, sort_keys=True, indent=4)
    print(d1)
    print(d2)
    print(d3)


def demo_dump():
    """
    把json字符串写入到json文件中

    """
    data = {'str3': 'liming', 'str2': 'xiaohong', 'str1': 'lilei'}
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def demo_load():
    """
    读取json文件转换为python数据字典格式

    """
    with open('data.json','r') as f:
        data = json.load(f)
        print(data)


demo_load()



