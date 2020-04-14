#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/4/12 12:15
"""
import xml.dom.minidom


def get_edge_list_by_parse_xml():
    # 通过解析xml文件,获取相应的有向边信息
    dom = xml.dom.minidom.parse("topology.xml")
    # 获取元素的根节点
    root = dom.documentElement
    # 找到子节点，得到的是一个数组
    states = root.getElementsByTagName('state')
    edge_list_ = []
    for state in states:
        widgets = state.getElementsByTagName('widgets')
        widget_list_ = widgets[0].getElementsByTagName('widget')
        for widget in widget_list_:
            center_x = widget.getElementsByTagName('center_x')
            center_x = center_x[0].childNodes[0].data
            print('center_x ', center_x)
            center_y = widget.getElementsByTagName('center_y')
            center_y = center_y[0].childNodes[0].data
            print('center_y ', center_y)
            from_value = widget.getElementsByTagName('from')
            from_value = from_value[0].childNodes[0].data
            print('from ', from_value)
            to_value = widget.getElementsByTagName('to')
            to_value = to_value[0].childNodes[0].data
            print('to ', to_value)
            edge_list_.append([center_x, center_y, from_value, to_value])
    print('边的详细信息：', edge_list_)
    return edge_list_


def get_node_list(edge_list_):
    # 获取对应的图结点信息，通过字典的形式返回
    node_list_ = []
    for i in edge_list_:
        node_list_.append(i[2])
    node_list_ = list(set(node_list_))
    new_node_list = {}
    new_widget_list = {}
    for i in node_list_:
        temp_node_list = []
        temp_widget_list = []
        for j in edge_list_:
            if i == j[2]:
                temp_node_list.append(j[3])
                temp_widget_list.append(j[0:2])
        new_node_list[i] = temp_node_list
        new_widget_list[i] = temp_widget_list
    print('结点的指向信息', new_node_list)
    print('结点的指向信息_权重', new_widget_list)
    return new_node_list, new_widget_list


def get_location_by_from_and_to(node_list_, widget_list_,  from_value, to_value):
    # 根据边的起始结点，获取widget的区域坐标
    for key in node_list_:
        if key == from_value:
            for node_value in node_list[key]:
                if node_value == to_value:
                    index = node_list[key].index(node_value)
                    return widget_list_[key][index]


def dfs(g, v, from_node):
    # 图的深度遍历
    visited.add(v)
    print("start")
    print('from', from_node)
    print('to', v)
    print('widget_location', get_location_by_from_and_to(node_list, widget_list, from_node, v))
    print("end\n")
    if v in g:
        for w in g[v]:
            if w not in visited:
                dfs(g, w, v)


if __name__ == '__main__':
    visited = set()
    edge_list = get_edge_list_by_parse_xml()
    node_list, widget_list = get_node_list(edge_list)
    dfs(node_list, '1', 'root')
