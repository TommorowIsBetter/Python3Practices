#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/12 15:23
"""
import json
from collections import Counter
dictionary = {'color': 'green', 'points': 5}
# 查询一个键值对
print(dictionary['color'])
print(dictionary)
# 添加一个键值对
dictionary['name'] = "name_test"
print(dictionary)
# 更新一个键值对
dictionary['color'] = 'red'
print(dictionary)
# 删除一个键值对
del dictionary['points']
print(dictionary)


# 把键值对写入txt文件中
str_name = 'WangYan'
str_sex = 'man'
file_name = 'WangYan' + '.txt'
dic = {'name': str_name,
       'sex': str_sex}
js = json.dumps(dic)
file = open(file_name, 'w')
file.write(js)
file.close()

# 读取txt中的字典
file = open(file_name, 'r')
js = file.read()
dic = json.loads(js)
print(dic)
file.close()

# 对字典进行排序
dic = {"Alice": 79, "Wad": 35, "Een": 25}
# 按照键的顺序来排序
list_key = sorted(dic.items(), key=lambda item: item[0])
print(list_key)
# 按照值的顺序来排序
list_value = sorted(dic.items(), key=lambda item: item[1])
print(list_value[-1][1] - list_value[-2][1])


# 对列表重复元素进行排序，并且获取具体的元素数量值
list_label = [2, 2, 2, 1, 2, 3, 3]
res = dict(Counter(list_label))
list_value = sorted(res.items(), key=lambda item: item[1])
print(list_value[-1][1] - list_value[-2][1])
