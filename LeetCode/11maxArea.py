#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/9/25 12:31
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxValue = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] > height[right]:
                value = height[right]*(right-left)
                right -= 1
            else:
                value = height[left]*(right-left)
                left += 1
            if value > maxValue:
                maxValue = value
        return maxValue


test = Solution()
testCase = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(test.maxArea(testCase))
