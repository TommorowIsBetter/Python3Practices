#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/9/24 20:46
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        label = 1
        if x < 0:
            label = -1
            x = x * label
        sum_ = 0
        temp = x
        num_length = 0
        while x != 0:
            x = int(x/10)
            num_length += 1
        num_length_temp = num_length
        list_before = []
        x = temp
        while x != 0:
            number = int(x / (10**(num_length-1)))
            list_before.append(number)
            x = x - number*(10**(num_length-1))
            num_length = num_length - 1
        for i in range(num_length_temp - len(list_before)):
            list_before.append(0)
        print(list_before)
        list_before.reverse()
        print(list_before)
        num_length = num_length_temp
        for i in list_before:
            sum_ = sum_ + i*(10**(num_length-1))
            num_length -= 1
        if sum_*label > 2147483648:
            return 0
        elif sum_*label < -2147483647:
            return 0
        else:
            return sum_*label


a = Solution()
print(a.reverse(100))