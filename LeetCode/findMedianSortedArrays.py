#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Wang Yan
@ide: PyCharm
@Time : 2019/9/8 12:16
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        list_ = nums1 + nums2
        list_.sort()
        length = len(list_)
        if length % 2 == 0:
            medianValue = (list_[int(length/2)] + list_[int(length/2 - 1)])/2.0
        else:
            medianValue = list_[int((length-1)/2)]
        return medianValue

nums1 = [1, 3]
nums2 = [2]
nums3 = [1, 2]
nums4 = [3, 4]
test = Solution()
print(test.findMedianSortedArrays(nums1, nums2))
print(test.findMedianSortedArrays(nums3, nums4))

