#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/9/7 20:23
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_value = 0
        sub_list = []
        for char in s:
            if char in sub_list:
                if max_value < len(sub_list):
                    max_value = len(sub_list)
                index_ = sub_list.index(char)
                sub_list = sub_list[index_ + 1:]
                sub_list.append(char)
            else:
                sub_list.append(char)
        if max_value < len(sub_list):
            max_value = len(sub_list)
        return max_value




test = Solution()
testCase_1 = "abcabcbb"
testCase_2 = "bbbb"
testCase_3 = "pwwkew"
testCase_4 = "dvdf"
testCase_5 = "anviaj"
testCase_6 = "jbpnbwwd"
testCase_7 = "bbtablud"
print(test.lengthOfLongestSubstring(testCase_1))
print(test.lengthOfLongestSubstring(testCase_2))
print(test.lengthOfLongestSubstring(testCase_3))
print(test.lengthOfLongestSubstring(testCase_4))
print(test.lengthOfLongestSubstring(testCase_5))
print(test.lengthOfLongestSubstring(testCase_6))
print(test.lengthOfLongestSubstring(testCase_7))



