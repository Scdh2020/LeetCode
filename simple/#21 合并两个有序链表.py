#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#21 合并两个有序链表.py
@time:2020/10/16
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    这题一开始是因为忘记了链表这个数据结构所以直接懵逼了，后面去补了一下链表结构后，就比较清楚了大概操作，都是还不够
    又去参考了一下官方题解，发现只需要创建一个头节点就能解决丢失问题（一开始自己想偏了，忽视了能创建节点这个点）
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建一个头节点
        headNode = ListNode(-1)
        # 创建一个游标
        cur = headNode
        # 只要其中一个为None说明另外一个有序链表中的值都比他大，只需在游标最后链上即可
        while l1 and l2:
            # 判断l1和l2当前节点值得大小，小的挂载到游标节点上，然后链表向后移动
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            # 游标向后移动
            cur = cur.next
        # 将不为None的链到游标节点
        cur.next = l1 if l1 is not None else l2
        # 返回头结点的下一个节点（头部是为了我们能找到后续节点）
        return headNode.next


if __name__ == '__main__':
    pass