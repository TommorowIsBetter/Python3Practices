#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/4/3 13:05
"""
# 一定要记得修改/etc/mongodb.conf里面的bind_ip=127.0.0.1改为0.0.0.0，这样才可从外部机器登陆。
# 用于读取MongoDB数据库里面的指定集合内容，然后加入到新的集合中去。
from pymongo import MongoClient
# 连接MongoDB的目标Ip地址，端口号为27017
client = MongoClient('192.168.1.100', 27017)
# 这里选择MongoDB的test的数据库
db = client.test
# 定义一个列表
dataset = []
# 查询col的数据并获得游标
cursor = db.col1.find({})
for doc in cursor:
    # 把_id属性去除，后面插入到新集合的时候会自动生成新的_id
    doc.pop('_id')
    doc.pop('jsonname')
    # 获取到的数据加入到列表中
    dataset.append(doc)
print("append over")
print(dataset)
# 对刚获得的列表进行遍历，然后把每个元素插入的新的集合col中
for doc in dataset:
    db.col.insert_one(doc)


