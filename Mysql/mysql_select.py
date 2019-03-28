#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/3/28 14:48
"""

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % (1000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        f_name = row[0]
        l_name = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("f_name=%s,l_name=%s,age=%s,sex=%s,income=%s" % \
              (f_name, l_name, age, sex, income))
except Exception as e:
    print(e)
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()