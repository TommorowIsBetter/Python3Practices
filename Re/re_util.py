#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/5/13 9:54
"""

import re

string = "2018年5月15日 8:29"
# 目标是取出里面的具体时间
result = re.findall(".*日 (.*)", string)
print(result[0])

string_time = "8:29"
# 目标是取出里面的数字8
hour = re.findall("(.*):.*", string_time)
print(hour[0])

last_line = "hserver2"
# 目标是取后面的数字2，下面是两种不同的匹配方式
number1 = re.findall("\d*\d", last_line)
number2 = re.findall("hserver(.*)", last_line)
print(number1[0])
print(number2[0])

string_name = "20190727080550_6_19.928.png"
# 目标是取出19.928这个具体的数字
index = string_name.split("_")[1]
index = int(index)
if index < 10:
    hover_time = re.findall("(?<=\d{14}_\d_).*?(?=\.png)", string_name)
elif 10 <= index < 100:
    hover_time = re.findall("(?<=\d{14}_\d{2}_).*?(?=\.png)", string_name)
elif 100 <= index < 1000:
    hover_time = re.findall("(?<=\d{14}_\d{3}_).*?(?=\.png)", string_name)
elif 1000 <= index < 10000:
    hover_time = re.findall("(?<=\d{14}_\d{4}_).*?(?=\.png)", string_name)
elif 10000 <= index < 100000:
    hover_time = re.findall("(?<=\d{14}_\d{5}_).*?(?=\.png)", string_name)
print(hover_time)


string_name_1 = "20190727080550_6_19.928.png"
# 目标是获取20190727080550_6_19.928这个子字符串
pre_name = re.findall(".*?(?=\.png)", string_name_1)[0]
print(pre_name)
