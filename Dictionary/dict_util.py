#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/12 15:23
"""

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
