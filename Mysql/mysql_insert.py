#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/3/28 14:42
"""

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except Exception as e:
    print(e)
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
