#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#67 二进制求和.py
@time:2020/10/24
"""


class Solution:
    """
    思路1：简答题简单解，用python内置函数，别弄花里胡哨的，何必程序员难为程序员呢...
    思路2：通过二进制0,1,进位，可以逆序相加的题解。有点忙，后面补上
    """
    def addBinary(self, a: str, b: str) -> str:
        # 将a,b转化为十进制
        a = int(a, 2)
        b = int(b, 2)
        # 十进制转化为二进制返回。[2:]去掉Python二进制中的0b
        return bin(a+b)[2:]


if __name__ == '__main__':
    a = Solution()
    print(a.addBinary("111", "111"))
