#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/4/6 13:40
该脚本的作用是当data node启动的时候，可以把data node的ip地址传到name node从而实现扩充的作用。
"""

import requests
import struct
import socket
import fcntl
import os
import time


def get_ip(ifconfig_name):
    """只需要指定网卡接口, 例如：eth0"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifconfig_name[:15]))[20:24])


def client_requests(request_url, request_data):
    """ 功能说明：发送json请求报文到指定的地址并获取请求响应报文, 输入参数说明：接收请求的URL，请求报文数据,格式为：
        {"param1":"123456","param2":"123456"} ,输出参数：请求响应报文 """

    request_json_data = str(request_data).replace("+", "%2B")
    request_data = request_json_data.encode("utf-8")
    head = {"Content-Type": "application/json; charset=UTF-8", 'Connection': 'close'}
    print('客户端请求JSON报文数据为（客户端 --> 服务端）:\n', request_data)
    # 客户端发送请求报文服务端
    r = requests.post(request_url, data=request_data, headers=head)
    # 获取服务端的响应报文数据
    respon_data = r.text
    print('服务端的响应报文为（客户端 <--服务端）: ', respon_data)
    print("get the status: ", r.status_code)
    # 返回请求响应报文
    return respon_data


# 获取本机ip地址
ip = get_ip('eth0')
# 把ip地址添加到json报文里面，准备传给服务器端
json_data = {'ip': ip}
response_data = client_requests("http://192.168.1.177:80/MapReduce/AnalysisJsonServlet", json_data)
print(response_data)
# 输出一些提示信息
print("now it is running. start datanode and nodemanager")
# 启动data node的datanode进程
os.system("/opt/hadoop/hadoop-2.8.5/sbin/hadoop-daemon.sh start datanode")
# 延时2秒钟启动node manager
time.sleep(2)
# 启动node manager
os.system("/opt/hadoop/hadoop-2.8.5/sbin/yarn-daemon.sh start nodemanager")


