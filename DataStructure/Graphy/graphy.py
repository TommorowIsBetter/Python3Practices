#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2020/4/11 12:34
"""


class Node(object):
    def __init__(self, value=None):
        self.value = value  # 结点的值
        self.come = 0  # 结点入度
        self.out = 0  # 结点出度
        self.next = []  # 结点的邻居结点
        self.edge = []  # 在结点为from的情况下，边的集合


class Edge(object):
    def __init__(self, fro, to, weight=None):
        self.weight = weight  # 边的权重
        self.fro = fro  # 边的from结点
        self.to = to  # 边的to结点


class Graph(object):
    def __init__(self):
        self.nodes = {}  # 图所有结点的集合，字典形式：{结点编号：结点}
        self.edges = []  # 图的边集合


def creatGraph(matrix):
    # 二维数组matrix [权重  从那个点的值  去哪个点的值]
    graph = Graph()
    # 建立所有结点
    for edge in matrix:
        weight = edge[0]
        fro = edge[1]
        to = edge[2]
        if fro not in graph.nodes:
            graph.nodes[fro] = Node(fro)
        if to not in graph.nodes:
            graph.nodes[to] = Node(to)
        # 建立所有的边
        fromNode = graph.nodes[fro]
        toNode = graph.nodes[to]
        newEdge = Edge(weight, fromNode, toNode)
        fromNode.next.append(toNode)  # 加上邻居指向
        fromNode.out += 1  # 出度+1
        toNode.come += 1  # 入度+1
        fromNode.edge.append(newEdge)
        graph.edges.append(newEdge)
    return graph
a = [[2, 4, 6],
     [3, 6, 5]]
print(creatGraph(a).nodes)
print(creatGraph(a).edges)

