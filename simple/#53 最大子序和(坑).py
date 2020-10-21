#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#53 最大子序和(坑).py
@time:2020/10/21
"""


class Solution:
    """
    我傻眼了好吧，一开始用暴力解法，结果超时了...
    由于算法底子不行就去看大佬们的题解，结果就是动态规划？分治法？贪心算法？
    于是我认真参考了一个动态规划题解（能读懂，就是缺基础理论），结果真香，真的是优雅高效。
    这里就留个坑，看书，看视频去。后续将动态规划、分治法、贪心这些算法原理都写一篇博客出来。然后题目都二刷，不懂算法做什么算法题，只会暴力破解（大力出奇迹...）
    """
    def maxSubArray(self, nums):
        # 当前最大连续子序列和
        sub_res = 0
        # 记录最大序列和
        res = nums[0]
        for i in range(len(nums)):
            # 如果当前最大连续子序列和大于零说明对后续有正向结果（更大）于是加上nums[i]
            if sub_res > 0:
                sub_res += nums[i]
            # 如果前最大连续子序列和小于等于零，说明反向结果（更小或无），于是更新sub_res
            else:
                sub_res = nums[i]
            # 更新最大子序和,始终保持最大
            res = max(sub_res, res)
        return res


if __name__ == '__main__':
    a = Solution()
    # print(max([-2,1,-3,4,-1,2,1,-5,4]))