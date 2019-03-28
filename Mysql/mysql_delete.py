#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/3/28 14:55
"""

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % 20
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except Exception as e:
    print(e)
    # 发生错误时回滚
    db.rollback()

# 关闭连接
db.close()
