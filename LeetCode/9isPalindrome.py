#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/9/23 19:31
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if 0 <= x <= 9:
            return True
        intX = str(x)
        m = 0
        a = int(len(intX) / 2)
        for i in range(a):
            m = i
            if intX[i] != intX[len(intX)-1 - i]:
                return False
        if m == (a - 1):
            return True
test = Solution()
testCase = -1221
print(test.isPalindrome(testCase))
