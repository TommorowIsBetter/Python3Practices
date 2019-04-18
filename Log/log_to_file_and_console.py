#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/4/18 21:45
"""

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logfile = 'my.log'
# 输出日志到文件，以append方式
file_handler = logging.FileHandler(logfile, mode='a')
# debug以上才输出到文件
file_handler.setLevel(logging.INFO)
# 输出到控制台
str_handler = logging.StreamHandler()
# info以上级别才输出到控制台
str_handler.setLevel(logging.INFO)
# 设置日志格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
# 日志格式添加到日志流
file_handler.setFormatter(formatter)
# 日志格式添加到控制台流
str_handler.setFormatter(formatter)
# 添加handler
logger.addHandler(file_handler)
# 添加handler
logger.addHandler(str_handler)
logger.info('this is a info message')

