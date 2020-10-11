#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#7 整数反转.py
@time:2020/10/11
"""


class Solution:
    """
    本题用简单易懂的字符串切片反转思路来处理
    """

    def reverse(self, x):
        # 首先将数字类型的x转化为字符串形式
        x = str(x)

        # 判断字符串是否带符号
        if x[:1] == "-":
            # 去掉负号，然后通过切片反转字符串，最后转化为int类型在加上负号 x[1:] => 去掉负号 x[1:][::-1] =>去掉负号后反转
            x = -int(x[1:][::-1])
        else:
            # 整数直接反转，会自动去掉数字前的0，例如：int('0321') => 321
            x = int(x[::-1])

        # 判断是否会溢出
        if (x >= 2147483647) or (x <= -2147483648):
            x = 0

        return x





if __name__ == '__main__':
    a = -12345
    print(Solution().reverse(a))
