#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#66 加一.py
@time:2020/10/23
"""


class Solution:
    """
    这题自己想的两个思路
    思路1：将列表转换为整形数字进行加一然后转换回整形列表
    思路2：逆序遍历列表将最后一位加1。会有两种情况：
        第一种最后一位是9或者不是9 是9变为0，不是9加1
        第二种列表都是9，进位的同事需要在最前面加1 [9,9] + 1 => [1,0,0](这种情况列表会比原来多一位)
    """
    def plusOne(self, digits):
        # 先将整形列表转换为字符串列表（[1,2,3] => ['1','2','3']）
        s = map(str, digits)
        # 拼接成为字符串(['1','2','3'] => '123')
        s = "".join(s)
        # 转换为整形并加1
        s = int(s) + 1
        # 将整形数字恢复为字符串
        s = str(s)
        # 将字符串转换为整形列表
        res = list(map(int, s))
        return res
        # return list(map(int, str(int(''.join(map(str, digits))) + 1)))

    def plusOne2(self, digits):
        # 记录最后的位置索引
        i = len(digits) - 1

        while True:
            # 第一种情况，等于9就赋值为0
            if digits[i] == 9:
                digits[i] = 0
            # 不是九就加一（相当于进位）
            else:
                digits[i] += 1
                break
            # 特殊情况，列表中都是9，结果上面的转换[9,9,9]会变为[0,0,0],满足下面条件 => [1,0,0,0]
            if digits[i] == 0 and i == 0:
                # 在列表左边插入1
                digits.insert(0, 1)
                break
            # 向左移动
            i -= 1
        return digits


if __name__ == '__main__':
    a = Solution()
    print(a.plusOne([9, 9, 9]))
    print(a.plusOne2([9, 9, 9]))
