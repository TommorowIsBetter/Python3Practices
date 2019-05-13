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
