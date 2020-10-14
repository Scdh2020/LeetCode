#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#14 最长公共前缀.py
@time:2020/10/14
"""


class Solution:
    '''
    这次没什么好的思路，就是用最憨的方法做出的，主要还是python函数储备少了，算法了解少了点。后面参考了一个不错的解法，大家可以对比一下，优雅的代码和憨憨（我的）代码的视觉体验。
    '''

    def longestCommonPrefix(self, strs):
        # 列表为空直接返回空字符串
        if not strs:
            return ''
        # 弹出一个字符串作为比较对象
        str1 = strs.pop()
        # 获取字符串长度（用来比较判断成功次数，全部成功才表示共有）
        list_len = len(strs)
        # 弹出字符串的索引值
        str1_index = 0
        # 记录共有字符串
        res = ''

        # 首先循环弹出的字符串长度次（因为共有开头不可能超过列表中任意一个字符串）
        while str1_index < len(str1):
            # 记录列表中每一个字符串公共前缀匹配成功次数
            flag = 0
            # 每次循环获取比较对象的前str1_index个字母（第一次获取第一个字母，第二场获取前2个字母以此类推）
            tmp = str1[0:str1_index+1]
            # 遍历需要判断的列表
            for str in strs:
                # 判断每一个字符串是否共有前缀tmp
                if str.startswith(tmp):
                    # 成功+1
                    flag += 1
            # 如果成功次数不等于列表长度说明不匹配，否则就匹配
            if flag != list_len:
                break
            else:
                res = tmp
            str1_index += 1
        return res

    def longestCommonPrefix2(self, strs):

        '''
        zip(*strs) 可以将里面的每一个字符串的字母都提取出来，组成元组列表，其中第一个元组是列表中每一个字符串的首字母组成
        例子：zip(*['abcde, 'abcd', 'abc', 'abd']) => [(a,a,a,a), (b,b,b,b), (c,c,c,d)]
        元组列表的长度是根据最短的字符串决定的，具体其他用途请自行查看文档
        '''

        # 用来保存结果
        res = ""
        # 循环zip生成的元组列表
        for tmp in zip(*strs):
            # set是将zip中的元组转化为集合（自动去重）
            tmp_set = set(tmp)
            # 如果len(tmp_set)大于1说明不属于公共前缀，因为转换为set自动去重后长度为1说明是共有的
            if len(tmp_set) == 1:
                # 连接赋值给res
                res += tmp[0]
            # 只要出现一个不是共有的，后面的就不用考虑
            else:
                break
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.longestCommonPrefix(["flower", "flow", "flight"]))
    print(a.longestCommonPrefix2(["flower", "flow", "flight"]))
