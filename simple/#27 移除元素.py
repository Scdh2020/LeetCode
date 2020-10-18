#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#27 移除元素.py
@time:2020/10/17
"""


class Solution:
    """
    这题的思考点和#26一样，需要判断哪些操作是原地，哪些不是，所以这题还会有双指针解法。
    第一个思路：一个就是直接通过Python中list remove操作，通过循环判断nums中是否还有重复，有就删除即可。
    第二个思路：双指针操作，i寻找不重复的，j作为起点，匹配到不重复的赋值给j，j加一，最终返回j的数目即可。
    """
    def removeElement(self, nums, val):
        # 循环判断val是否在nums中，直到不存在就退出循环
        while val in nums:
            # 删除一次重复的值
            nums.remove(val)
        # 剩下的结果都不重复，所以直接返回剩余长度
        return len(nums)

    def removeElement2(self, nums, val):
        nums_len = len(nums)
        # 寻找不重复的index（快指针）
        i = 0
        # 作为不重复的index（慢指针）
        j = 0
        while i < nums_len:
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j


if __name__ == '__main__':
    a = Solution()
    print(a.removeElement([1, 1, 2], 1))
    print(a.removeElement2([1, 1, 2], 1))
