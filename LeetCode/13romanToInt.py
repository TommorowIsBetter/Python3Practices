#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/9/24 16:43
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum_ = 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = list(s)
        temp = -1
        for i in range(len(s)):
            if i == temp:
                continue
            if i <= len(s) - 2:
                if dic[s[i]] < dic[s[i+1]]:
                    temp = i + 1
                    value = dic[s[i+1]] - dic[s[i]]
                else:
                    value = dic[s[i]]
                sum_ = sum_ + value
        if dic[s[len(s) - 1]] <= dic[s[len(s) - 2]]:
            value = dic[s[len(s) - 1]]
            sum_ = sum_ + value
        return sum_


a = Solution()
print(a.romanToInt("MCMXCIV"))
