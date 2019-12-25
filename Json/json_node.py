#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/25 19:36
"""
import json
import sys
import io
node_list = []
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def get_all_children(node_):
    # 递归方式获取所有的子节点
    if len(node_['children']) == 0:
        node_list.append(node_)
    else:
        for i_ in node_['children']:
            get_all_children(i_)

def get_all_leaf_node(json_file_):
    with open(file=json_file_, mode='r', encoding='utf8') as data_file:
        content = json.load(data_file)
        for i_ in content['nodeList']:
            get_all_children(i_)

if __name__ == "__main__":
    json_file = '20191225165548061.json'
    get_all_leaf_node(json_file)
    for i in node_list:
        print(i)
