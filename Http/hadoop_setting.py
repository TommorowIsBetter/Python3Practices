#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/4/13 14:38
该脚本的作用是实例创建完之后，自动重新启动主机，以使得服务保持正常
"""

import os
import ConfigParser
config = ConfigParser.ConfigParser()
config.read("/opt/hadoop_setting.ini")
label = config.get("reboot", "label")
if label == "0":
    # 使得label标签设置为1，否则会一直进行循环
    config.set("reboot", "label", "1")
    config.write(open("/opt/hadoop_setting.ini", "w"))
    # 重新启动系统
    os.system("/sbin/reboot")
