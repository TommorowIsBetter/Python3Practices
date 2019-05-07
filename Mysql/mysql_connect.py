#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/3/27 21:55
"""
# 一定要记得修改/etc/mysql/my.cnf下的bind-address = 127.0.0.1改为0.0.0.0，这样才允许外部连接，否则mysql不允许外部访问。
import pymysql

# 打开数据库连接
db = pymysql.connect("192.168.1.100", "root", "root", "mysql", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()
