#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#26 删除排序数组中的重复项.py
@time:2020/10/16
"""


class Solution:
    """
    这题解法，由于我不太确定那种操作不是原地修改的，所以我直接参考了官方的双指针解法。

    i表示慢指针、j表示快指针
    1.nums[i] == nums[j] 时j+1跳过重复
    2.nums[i] != nums[j] 说明遇到不重复的，需要 i+=1，nums[i] = nums[j]，j+=1
    3.循环1,2操作
    4.最后不重复的长度就是i+1
    """
    def removeDuplicates(self, nums):
        nums_len = len(nums)
        if nums_len == 0:
            return 0

        # i代表冲第一个元素开始，j代表第二个元素开始
        i, j = 0, 1

        while j < nums_len:
            # 判断不重复则覆盖重复的位置
            if nums[j] != nums[i]:
                i += 1  # i+1就是重复的位置
                # 覆盖重复
                nums[i] = nums[j]
            j += 1

        return i+1


if __name__ == '__main__':
    a = Solution()
    print(a.removeDuplicates([1,2,3,4,4]))