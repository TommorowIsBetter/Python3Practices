#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/4/10 21:08
该脚本的作用是让name node开机时候实现自启动hadoop，所以就要设置/etc/hosts，而hadoop/slaves可以为空，只启动name_node结点。
"""

import struct
import socket
import fcntl
import os
import time

def get_ip(ifconfig_name):
    """只需要指定网卡接口, 例如：eth0"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifconfig_name[:15]))[20:24])


def set_hosts(ip_address):
    """ 更新hosts文件，把/etc/hosts的第一行位置设置为name node的ip和主机名的映射 """
    lines = []
    with open('/etc/hosts', 'r') as f:
        for line in f:
            lines.append(line)
    ip_name =ip_address + " " + "hserver1" + "\n"
    if len(lines) == 2:
        lines.append(ip_name)
    else:
        lines[2] = ip_name
    with open('/etc/hosts', 'w+') as f:
        for line in lines:
            f.write(line)
    print(lines)


def hserver1_is_exist():
    """  判断hserver1是否存在"""
    with open('/opt/hadoop/hadoop-2.8.5/etc/hadoop/slaves', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.strip("\n") == "hserver1":
            return True
    return False


def add_salves():
    """ 更新salves文件，插入新添加到hadoop集群的机器名字 """
    with open('/opt/hadoop/hadoop-2.8.5/etc/hadoop/slaves', 'a') as f:
        if hserver1_is_exist() is False:
            f.write("hserver1\n")


# 获得主机当前ip地址
ip = get_ip('eth0')
# 设置/etc/hosts
set_hosts(ip)
# 添加相应的hserver1到hadoop/slaves下面
add_salves()
# 启动hadoop集群
# os.system("/opt/hadoop/hadoop-2.8.5/sbin/start-all.sh")
# 通过函数可以返回具体的值来判断hadoop集群是否启动
result = os.popen("jps | grep NameNode | wc -l").read()
print "result:" + result
# 如果为2,则Name node进程已经正常启动，如果不是，则循环知道hadoop正常
while int(result) != 2:
    time.sleep(5)
    os.system("/opt/hadoop/hadoop-2.8.5/sbin/start-all.sh")
    result = os.popen("jps | grep NameNode | wc -l").read()
