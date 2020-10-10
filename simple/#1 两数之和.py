#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#1 两数之和.py
@time:2020/10/10
"""

class Solution:
    """
    主要思路就是用target减去列表中的每一个元素，查看其差值是否在剩余的列表中，如果在则获取下标即可
    """
    def twoSum(self, nums, target):
        # 首先循环列表个数次
        for x in range(len(nums)):
            # 用target减去当前循环的元素
            tmp = target - nums[x]
            # 判断相减得到的值是否在列表中
            if tmp in nums:
                # 在的话就获取下标
                y = nums.index(tmp)
                # 判断下标是否和当前元素相同，相同则不能采用
                if y == x:
                    continue
                return x, y

