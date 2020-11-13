#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#125 验证回文串.py
@time:2020/11/13
"""

"""
这题比较简单，就直接用自己的思路发出来，看了一下比较简洁的思路基本上都是以下几点：1.转小写 2.去符号 3.反转比较
"""
import re

class Solution:
    def isPalindrome(self, s):
        # 正则表达式去除特殊符号     字符串转小写
        s = re.sub('[\W|_]', '', s.lower())
        # 正向与反向比较并返回比较结果
        return s == s[::-1]


if __name__ == '__main__':
    a = Solution()
    print(a.isPalindrome("A man, a plan, a canal: Panama"))
