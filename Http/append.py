#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/4/6 15:10
该脚本的作用是把新加入结点ip地址和对应的主机名写入到/etc/hosts文件中，然后在hadoop/slaves也写入相应的内容。
"""
import re
import sys
import os
import time


def get_hserver_name():
    """ 获取最新的hserver名字，例如hserver4"""
    with open('/opt/hadoop/hadoop-2.8.5/etc/hadoop/slaves', 'r') as fp:
        lines = fp.readlines()
        if len(lines) != 0:
            last_line = lines[-1]
    if len(lines) != 0:
        number = re.findall("\d*\d", last_line)
        number_order = int(number[0]) + 1
        base_str = "hserver"
        machine_name = base_str + str(number_order) + "\n"
    else:
        machine_name = "hserver2" + "\n"
    return machine_name


def get_hserver_host_name():
    """ 获取最新的hserver名字，例如hserver4"""
    with open('/opt/hadoop/hadoop-2.8.5/etc/hadoop/slaves', 'r') as fp:
        lines = fp.readlines()
        if len(lines) != 0:
            last_line = lines[-1]
    if len(lines) != 0:
        number = re.findall("\d*\d", last_line)
        number_order = int(number[0]) + 1
        base_str = "hserver"
        machine_name = base_str + str(number_order)
    else:
        machine_name = "hserver2"
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


def is_exist(ip_address):
    """ 判断新加入的主机ip地址是否已经在/etc/hosts文件中 """
    lines = []
    with open('/etc/hosts', 'r') as f:
        for line in f:
            lines.append(line)
    for line in lines:
        for i in line.split():
            if i == ip_address:
                return True
    return False


# 获取外部传入过来的参数
ip = sys.argv[1]
# 在/etc/hosts文件中添加新加机器的记录
if is_exist(ip) is False:
    add_hosts(ip)
    # 在/hadoop/slaves中添加新加机器的记录
    add_salves()
# 关闭hadoop集群系统
os.system("/opt/hadoop/hadoop-2.8.5/sbin/stop-all.sh")
# 在这里延时10s钟
time.sleep(10)
# 重新启动hadoop系统,即可在web界面查看到新加入到机器中的结点
os.system("/opt/hadoop/hadoop-2.8.5/sbin/start-all.sh")


