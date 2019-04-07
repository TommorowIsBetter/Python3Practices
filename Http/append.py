#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/4/6 15:10
"""
import re
import sys


def get_hserver_name():
    """ 获取最新的hserver名字，例如hserver4"""
    with open('/opt/hadoop/hadoop-2.8.5/etc/hadoop/slaves', 'r') as fp:
        lines = fp.readlines()
        last_line = lines[-1]
    number = re.findall("\d*\d", last_line)
    number_order = int(number[0]) + 1
    base_str = "hserver"
    machine_name = base_str + str(number_order) + "\n"
    return machine_name


def get_hserver_host_name():
    """ 获取最新的hserver名字，例如hserver4"""
    with open('/opt/hadoop/hadoop-2.8.5/etc/hadoop/slaves', 'r') as fp:
        lines = fp.readlines()
        last_line = lines[-1]
    number = re.findall("\d*\d", last_line)
    number_order = int(number[0]) + 1
    base_str = "hserver"
    machine_name = base_str + str(number_order)
    return machine_name


def add_salves():
    """ 更新salves文件，插入新添加到hadoop集群的机器名字 """
    machine_name = get_hserver_name()
    with open('/opt/hadoop/hadoop-2.8.5/etc/hadoop/slaves', 'a') as f:
        f.write(machine_name)


def add_hosts(ip_address):
    """ 更新hosts文件，插入新添加到hadoop集群的机器Ip地址和主机名字 """
    machine_name = get_hserver_host_name()
    record_host = ip_address + " " + machine_name + "\n"
    with open('/etc/hosts', 'a') as f:
        f.write(record_host)


# 获取外部传入过来的参数
ip = sys.argv[1]
# 在/etc/hosts文件中添加新加机器的记录
add_hosts(ip)
# 在/hadoop/slaves中添加新加机器的记录
add_salves()

