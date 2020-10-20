#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#38 外观数列.py
@time:2020/10/20
"""


class Solution:
    """
    这题用的是双指针来做的，我这个写法效率比较低，后面准备参考一下别的双指针解法和递归解法，更新一下题解。
    """
    def countAndSay(self, n):
        res = "1"

        # 循环n-1次（因为第一次已经默认是1了）
        for _ in range(n-1):
            # 设置开始指针和结尾指针（用来寻找重复的字符串 例如：111 => (e_index-s_index)+res[s_index] => str(3-0)+'1' => 31）
            s_index = e_index = 0
            tmp = ""
            res_len = len(res)
            while res_len >= e_index:
                # 判断连续的重复字符串
                if res[s_index] == res[e_index:e_index+1]:
                    e_index += 1
                # 不重复且不为空时（说明连续的重复结束了）
                elif res[e_index:e_index+1] != "":
                    # 计算当前外观描述（111 => 31）
                    tmp += str(e_index - s_index)+res[s_index]
                    # 开始指针后移（例如 1112 这个时候s_index对应位置应该是'2'）
                    s_index = e_index
                # 字符串到了尾
                else:
                    # 同上
                    tmp += str(e_index-s_index) + res[s_index]
                    # 结束这次循环
                    break
            res = tmp
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.countAndSay(1))
    print(a.countAndSay(2))
    print(a.countAndSay(3))
    print(a.countAndSay(4))
    print(a.countAndSay(5))
