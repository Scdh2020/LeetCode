#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#35 搜索插入位置(坑).py
@time:2020/10/19
"""
class Solution:
    """
    这题先用一个大家通常能想到的题解先提交了，后续我抽空会把其他解法补充上（各种查找算法），该题会持续更新。
    """
    def searchInsert(self, nums, target):
        nums.append(target)
        nums.sort()
        return nums.index(target)


if __name__ == '__main__':
    a = Solution()
    print(a.searchInsert([1,3,5,6], 5))