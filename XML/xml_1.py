#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/9/25 14:30
"""
import xml.etree.ElementTree as ET
tree = ET.ElementTree(file='window_dump.xml')
root = tree.getroot()
result_list = []
queue = [root]
while queue:
    count = 0
    size = len(queue)
    temp_list = []
    while count < size:
        node = queue.pop()
        temp_list.append(node)
        for child in node:
            queue.insert(0, child)
        count += 1
    result_list.append(temp_list)
for i in result_list:
    print(len(i), i)
