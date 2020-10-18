#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#28 实现strStr().py
@time:2020/10/18
"""


class Solution:
    """
    这题两个思路：
    第一个没什么好说的，就是Python的字符串内置函数find完美复合题目要求。
    第二就是比较基础的做法了，首先把0和-1的情况判断掉，然后循环查找字符串的长度次，最后就是不断匹配了。例子如下
    例子：hello   ll     i=0
        判断 he == ll  不匹配  i+=1   i->1
        判断 el == ll  不匹配  i+=1   i->2
        判断 ll == ll  匹配   返回2
    """

    def strStr(self, haystack, needle):
        return haystack.find(needle)

    def strStr2(self, haystack, needle):
        if needle not in haystack:
            return -1

        if needle == "":
            return 0

        needle_len = len(needle)
        # 记录index
        i = 0
        # 循环haystack的字符串长度次
        for _ in range(len(haystack)):
            # 切needle的长度的字符串来匹配
            if haystack[i:i+needle_len] == needle:
                return i
            i += 1



if __name__ == '__main__':
    a = Solution()
    print(a.strStr2("hello", "ll"))
    # print(a.strStr("aaaaa", "bba"))
    # print(a.strStr("aaaaa", ""))
