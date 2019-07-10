#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/12 15:23
"""
import json
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
