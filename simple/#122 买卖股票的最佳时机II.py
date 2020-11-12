#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#122 买卖股票的最佳时机II.py
@time:2020/11/12
"""

"""
这一题参考了一下大佬题解，漂亮的解法，且思路简单：只要所有上涨交易日都卖就能达到收益最大。
"""
class Solution:
    def maxProfit(self, prices):
        # 记录累积收益
        profit_max = 0
        # 从第二天开始（第二天-前一天 = 收益）
        for i in range(1, len(prices)):
            # 计算收益
            profit = prices[i] - prices[i-1]
            # 只要为正即可累加
            if profit > 0:
                profit_max += profit
        return profit_max


if __name__ == '__main__':
    a = Solution()
    print(a.maxProfit([7,1,5,3,6,4]))