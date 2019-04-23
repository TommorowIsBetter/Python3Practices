#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/4/23 15:25
"""

# 引入selenium
from selenium import webdriver
# 使用webkit无界面浏览器
# 如果路径为 exe 启动程序的路径，那么该路径需要加一个 r,需要设置phantomjs.exe的环境变量
driver = webdriver.PhantomJS()
# 获取指定网页的数据  start_urls
driver.get('http://news.sohu.com/scroll/')
print(driver.find_element_by_class_name('title').text)
