#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#9 回文数.py
@time:2020/10/12
"""


class Solution:
    """
    本题最简单的做法就是利用字符串反转即可，
    如果需要满足进阶要求不转换字符串的话可以用取模的方式来完成。
    """
    # 字符串处理方式
    def isPalindrome(self, x):
        # 首先转换为字符串
        str_x = str(x)
        # 用字符串和反转之后的字符串进行比较即可（str_x[::-1]反转字符串）
        if str_x == str_x[::-1]:
            return True
        else:
            return False

    # 取模方式处理
    def isPalindromePush(self, x):
        """
        原理说明：例如判断121是否为回文数则可以通过如下取模方式进行（正确的例子）
                121%10  => 1   拼接得到的结果 x = 1
                12%10   => 2   拼接得到的结果 x = 12
                1%10    => 1   拼接得到的结果 x = 121
                121 = 121 结果正确

                例如判断123是否为回文数则可以通过如下取模方式进行（错误的例子）
                123%10  => 3   拼接得到的结果 x = 3
                12%10   => 2   拼接得到的结果 x = 32
                1%10    => 1   拼接得到的结果 x = 321
                123 != 321 结果错误
        """
        # 根据题目要求负数一定不是回文数
        if x < 0:
            return False

        # 记录取模后剩下的数字
        tmp = x
        # 记录拼接后的数字
        res = 0
        # 循环取模得到反转后的数字
        while tmp > 0:
            # 拼接数字  123举例  (0*10)+(123%10)=3、 (3*10)+(12%10)=32、 (32*10)+(1%10)=321
            res = (res*10) + (tmp % 10)
            # 整数除法  123举例 123//10=12、 12//10=1  1//10=0
            tmp = tmp//10

        # 判断拼接后的是否等于原数字
        if res == x:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Solution()
    print(a.isPalindrome(123))
    print(a.isPalindrome(12321))
    print(a.isPalindromePush(123))
    print(a.isPalindromePush(12321))
