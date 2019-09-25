#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/9/6 21:07
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        p1_list = []
        p2_list = []
        while p1 is not None:
            p1_list.append(p1.val)
            p1 = p1.next
        len_1 = range(len(p1_list))
        value_1 = 0
        for item, index in zip(p1_list, len_1):
            value_1 = value_1 + (item * 10 ** index)

        while p2 is not None:
            p2_list.append(p2.val)
            p2 = p2.next
        len_2 = range(len(p2_list))
        value_2 = 0
        for item, index in zip(p2_list, len_2):
            value_2 = value_2 + (item * 10 ** index)
        print(value_1)
        print(value_2)
        sum_ = value_1 + value_2
        list_2 = list(str(sum_))
        for i in range(len(list_2)):
            list_2[i] = int(list_2[i])
        list_2 = list(reversed(list_2))
        head = ListNode(list_2[0])
        p = head
        for i in list_2[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return head

p1 = ListNode(2)
p2 = ListNode(4)
p3 = ListNode(3)
p1.next = p2
p2.next = p3

p4 = ListNode(5)
p5 = ListNode(6)
p6 = ListNode(4)
p4.next = p5
p5.next = p6

a = Solution()
print(a.addTwoNumbers(p1, p4))
