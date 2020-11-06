#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#83 删除排序链表中的重复元素.py
@time:2020/11/05
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    这题了解一下链表这个数据结构就比较简单，思路理不清楚纸上画一画就明白了哈
    我的思路就是通过基础遍历，判断前一位与后一位是否重复，重复就前一位跳过后一位
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 创建一个变量指向链表开头
        headNode = head
        # 创建一个游标是前一位（用于前一位与后一位比较是否重复）
        cur = head
        if head:
            # 后移一位
            head = head.next
        while head:
            # 前一位与后一位比较
            if cur.val == head.val:
                # 前一位的next直接链接至下一位的next（跳过重复）
                cur.next = head.next
            else:
                cur = cur.next
            # 后移一位
            head = head.next
        return headNode

if __name__ == '__main__':
    pass