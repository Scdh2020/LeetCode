#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#20 有效的括号.py
@time:2020/10/15
"""


class Solution:
    """
    做这题前我了解了一下括号匹配思路，比较常规的就是通过入栈出栈的方式。
    简单来说入栈出栈的方式就是：先遍历字符串的每一个字符，判断是否是左括号，如果是左括号就入栈，当匹配到右括号时，
    就弹出栈中的一个左括号来匹配，由于栈的特点后进先出所以最后入栈的左括号一定是和出现的这个右括号匹配的。
    举例1："{()}" '{'=>入栈，'('=>入栈，')'=>出栈'('匹配')'，'}'=>出栈'{'匹配'}'  => True
    举例2："{()]" '{'=>入栈，'('=>入栈，')'=>出栈'('匹配')'，'}'=>出栈'{'不匹配']'  => False
    """

    def isValid(self, s):
        rule = {'{': '}', '[': ']', '(': ')'}
        stack = []

        for item in s:
            # 判断是否为左括号
            if item in rule.keys():
                # 左括号入栈
                stack.append(item)
            # 若不是左括号且栈中有括号
            elif stack:
                # 弹出最后进入的括号
                left = stack.pop()
                # 括号匹配，成功则继续循环
                if item != rule[left]:
                    return False
            # 又不是左括号且栈中无括号，故直接返回False（因为遍历到的这个半括号，既不是左括号栈中也没有左括号匹配，所以直接返回False）
            else:
                return False

        # 判断栈是否为空，为空说明全部匹配成功
        if not stack:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Solution()
    print(a.isValid('[{}[]{}(([]))]'))
    print(a.isValid('[{}[]{})([]))]'))