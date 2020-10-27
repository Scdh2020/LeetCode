#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#69 x的平方根(坑).py
@time:2020/10/27
"""


class Solution:
    """
    之后做题我还是秉承简答题简单做的理念来进行题解（好吧，其实我比较忙，还要其他事）。然后在花时间将其他解法在后面在补上。
    这题不用函数，直接使用python **乘方运算符解决，平方根相当于x的0.5次方，然后int取整即可
    """
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)


if __name__ == '__main__':
    a = Solution()
    print(a.mySqrt(8))