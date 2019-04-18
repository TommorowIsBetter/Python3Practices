#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/4/18 21:43
"""

import logging

logging.basicConfig(
                    # 控制台打印的日志级别
                    level=logging.DEBUG,
                    # 日志的文件名
                    filename='new.log',
                    # 模式有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志,a是追加模式，默认追加模式
                    filemode='a',
                    # 日志格式
                    format='%(asctime)s - [line:%(lineno)d] - %(levelname)s: %(message)s'
                    )

logging.info("this is a info")