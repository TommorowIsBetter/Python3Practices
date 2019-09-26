#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/9/26 10:38
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        sum_1 = []
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        length = len(digits)
        if length == 0:
            return []
        if length == 1:
            for i in dic[digits]:
                sum_1.append(i)
            return sum_1
        list_ = ['-1']*length
        for i in range(length):
            list_[i] = dic[digits[i]]
        sum_1 = list(list_[0])
        temp_list = []
        for i in range(len(list_))[1:]:
            for k in list_[i]:
                for j in sum_1:
                    temp = j+k
                    temp_list.append(temp)
            del sum_1[:]
            sum_1 = temp_list[:]
            del temp_list[:]
        return sum_1


test = Solution()
testCase = "23"
print(test.letterCombinations(testCase))