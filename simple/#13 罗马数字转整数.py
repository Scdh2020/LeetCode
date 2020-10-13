#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#13 罗马数字转整数.py
@time:2020/10/13
"""


class Solution:
    """
    这题自己的做法比较常规，有点带偷懒的情况...就是将非重复的组合都提前放入字典中，然后循环判断字典中的key是否在字符串中出现，出现就相加出现的次数，并在字符串中去掉对应key出现的次数
    """
    def romanToInt(self, s):
        # 记录累加值
        res = 0
        # 规则字典
        rule = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4, 'M': 1000,
                'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        # 循环整个字典
        for key, value in rule.items():
            # 如果字典中的key在字符串s中有出现则进入
            if key in s:
                # 统计字典中的key在字符串中出现的次数。例如：III 是 1*3=3
                key_count = s.count(key)
                # 计算累加值
                res += (value * key_count)
                # 字符串替换，将计算过的符号替换为空字符串
                s = s.replace(key, '', key_count)
                # 如果字符串s为空字符串后说明计算完成
                if s == '':
                    break
        return res

    def romanToInt2(self, s):
        # 记录累加值
        res = 0
        # 规则字典
        rule = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # 记录字符串长度
        s_len = len(s)
        # 循环字符串长度减1次（因为需要判断字符串前一位与后一位字符对应规则字典的大小关系，不减1的话最后一位字符是没有下一位的）
        for index in range(s_len - 1):
            # 判断第一位字符是否小于第二位（按照规则如果前一位字符比后一位字符小则减前一位，否则加前一位）
            if rule[s[index]] < rule[s[index+1]]:
                res -= rule[s[index]]
            else:
                res += rule[s[index]]
        # 最后返回累加值时需要注意，把字符串最后一位加上
        return res + rule[s[-1]]




if __name__ == '__main__':
    a = Solution()
    print(a.romanToInt('XLIV'))
    print(a.romanToInt2('XLIV'))