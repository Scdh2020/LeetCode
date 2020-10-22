#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:58.最后一个单词的长度.py
@time:2020/10/22
"""


class Solution:
    """
    这题就比较简单点了，第一种思路是想到了用Python内置函数通过空格分割字符串为列表，然后取出最后一个元素求出长度即可。
    第二种思路是通过双指针逆序循环找字符串的方式（这个参考了别人的题解）
    """
    def lengthOfLastWord(self, s):
        # 工具空格字符串分割（例如：hello world => ['hello','world]）
        s_list = s.split()
        # 列表长度
        s_list_len = len(s_list)
        # 排除空列表
        if s_list_len == 0:
            return 0
        # 返回列表最后一个元素的长度
        return len(s_list[s_list_len-1])

    def lengthOfLastWord2(self, s):
        # 去除末尾空格
        s = s.rstrip()
        # 记录指逆序针位置（end不用动，因为已经去除了空格）
        start = end = len(s) - 1
        # 字符串从右到左判断，直到字符串为空格或到头了就退出
        while start >= 0 and s[start] != ' ':
            start -= 1
        # 字符串长度就是末尾减去start指针的位置
        return end - start


if __name__ == '__main__':
    a = Solution()
    print(a.lengthOfLastWord("   abc   "))
    print(a.lengthOfLastWord2("   abc   "))
