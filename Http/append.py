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
import subprocess


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


def scp_remote(user, password, ip, localsource, remotedest, port=22):
    """ 向远程ip地址scp文件过去  """
    scp_cmd_base = r"""
            expect -c "
            set timeout 300 ;
            spawn scp -P {port} -r {localsource} {username}@{host}:{remotedest} ;
            expect *assword* {{{{ send {password}\r }}}}  ;
            expect *\r ;
            expect \r ;
            expect eof
            "
    """.format(username=user, password=password, host=ip, localsource=localsource, remotedest=remotedest, port=port)
    SCP_CMD = scp_cmd_base.format(localsource=localsource)
    print("execute SCP_CMD: ", SCP_CMD)
    p = subprocess.Popen(SCP_CMD, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.communicate()
    os.system(SCP_CMD)


def is_ip(str_ip):
    """  该函数的作用是判断一个字符串是否是ip地址"""
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(str_ip):
        return True
    else:
        return False


def get_ip_list():
    """ 获取连接到name node结点的所有data node结点的ip地址 """
    # lines列表代表读取的/etc/hosts的所有行
    lines = []
    # ips列表用于存储所有的data node的ip地址
    ips = []
    with open('/etc/hosts', 'r') as f:
        for line in f:
            lines.append(line)
    for line in lines[2:]:
        for i in line.split():
            if is_ip(i) is True:
                ips.append(i)
    return ips


def scp_all_remote(ip_list):
    """ 向所有的data node传送/etc/hosts文件"""
    for ip in ip_list:
        scp_remote("root", "123456", ip, "/etc/hosts", "/etc/", 22)


# 获取外部传入过来的参数
ip = sys.argv[1]
# 在/etc/hosts文件中添加新加机器的记录
if is_exist(ip) is False:
    add_hosts(ip)
    # 在/hadoop/slaves中添加新加机器的记录
    add_salves()
    # 获取所有的data node的ip地址
    ip_lists = get_ip_list()
    # 向所有的data node传送/etc/hosts
    scp_all_remote(ip_lists)
    # 刷新nodes，是data node加入进来可以显示
    os.system("hdfs dfsadmin -refreshNodes")



