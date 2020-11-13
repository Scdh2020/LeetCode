#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#121 卖股票的最佳时机.py
@time:2020/11/11
"""


class Solution:
    """
    本题自己的解法和官方的解法，自己写的解法直接用双指针来操作的，官方解法通过比较当前最小值和当前最大收益来更新迭代寻找最大收益
    """
    def maxProfit(self, prices):
        """
        首先定义卖出价指针和买入价指针，循环判断卖出价-买入价的状态来判断当前最小买入价和更新最大收益
        例子[9,1,8,2]
        第一次循环：profit_max=0, p1=>9, p2=>1, 1-9=-8 为负数说明当前p2更适合买入于是 p1=>1 p2后移一位=>8
        第二次循环：profit_max=0, p1=>1, p2=>8, 8-1=7  7>0（profit_max）更新当前最大值 p2后移一位=>2
        第三次循环：profit_max=7, p1=>1, p2=>2, 2-1=1  1>7（profit_max）不操作，p2继续后移=>None
        循环结束(p2=l)
        返回7
        """
        # 定义双指针（p2卖出价）
        p1 = 0
        p2 = 1
        # 定义最大收益
        profit_max = 0
        l = len(prices)
        while p1 < l and p2 < l:
            # 计算盈利（卖出价（p2）-买入价（p1））
            profit = prices[p2] - prices[p1]
            # 盈利小于零说明p2为买入价的话更合适
            if profit < 0:
                # 买入价p1跳到p2去
                p1 = p2
            # 盈利如果大于了定义最大收益则更新当前最大收益
            elif profit > profit_max:
                profit_max = profit

            # 卖出价p2向下继续寻找合适卖出价
            p2 += 1
        return profit_max

    def maxProfit2(self, prices):
        """
        循环过程中会找到最小的买入价，然后通过循环中比较卖出价-当前最小买入价，不断更新最大收益
        例如[9,1,8,2]
        第一次循环：minprice=9，maxprofit=max(0,9-9)=>0
        第二次循环：minprice=1，maxprofit=max(0,1-1)=>0
        第三次循环：minprice=1，maxprofit=max(0,8-1)=>7
        第四次循环：minprice=9，maxprofit=max(7,2-1)=>7
        输出7
        """
        # 记录买入价（最小）（默认为大一点的数字）
        minprice = int(1e9)
        # 记录最大股票收益
        maxprofit = 0
        # 遍历数组
        for price in prices:
            # 记录每次的最小价格
            minprice = min(minprice, price)
            # 更新最大收益
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit


if __name__ == '__main__':
    a = Solution()
    print(a.maxProfit([7,1,5,3,6,1]))
    print(a.maxProfit([2,1,2,1,0,1,2]))
    print(a.maxProfit2([7, 1, 5, 3, 6, 1]))
    print(a.maxProfit2([2,1,2,1,0,1,2]))
    print(a.maxProfit2([1,2,3,4,5]))