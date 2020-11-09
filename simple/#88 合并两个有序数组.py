#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Scdh
@file:#88 合并两个有序数组.py
@time:2020/11/09
"""

"""
自己思路是双指针，但是想歪了，写出了一个双循环....所以就没贴出来了，然后看了官方题解后感慨，遇到数组题还是先考虑双指针！
"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        简介：直接合并，然后查询排序
        时间复杂度：O( (n+m)log(n+m) )
        空间复杂度：O(1)
        """
        nums1[:] = sorted(nums1[:m] + nums2)

    def merge2(self, nums1, m, nums2, n):
        """
        简介：双指针 => 前到后
        时间复杂度：O(n+m)
        空间复杂度：O(m)
        """
        # 记录有值的列表
        nums1_tmp = nums1[:m]
        # 清空nums1
        nums1[:] = []

        # 双指针分别指向nums1和nums2的开头
        p1 = 0
        p2 = 0

        # 循环判断，（条件为不能不能超过各种的值）
        while p1 < m and p2 < n:
            # 将小的值添加入清空过的nums1中
            if nums1_tmp[p1] < nums2[p2]:
                nums1.append(nums1_tmp[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # 分别判断p1和p2指针，将剩下的值加入nums1中
        if p1 < m:
            nums1[p1 + p2:] = nums1_tmp[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

    def merge3(self,  nums1, m, nums2, n):
        """
        简介：双指针 => 后到前
        时间复杂度：O(n+m)
        空间复杂度：O(1)
        """
        #  双指针分别指向nums1和nums2有值的尾部
        p1 = m - 1
        p2 = n - 1
        # 用来记录nums1最后一个位置（空位的最后一个）
        p = m + n - 1

        # 循环判断（条件为指针最多到列表头）
        while p1 >= 0 and p2 >= 0:
            # 尾部值比较（大的说明最大，直接添加入nums1[p]最后一个位置上 ）
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        # 补齐nums2遗漏的值
        nums1[:p2 + 1] = nums2[:p2 + 1]










if __name__ == '__main__':
    a = Solution()
    # a.merge([4,0,0,0,0,0], 1, [1,2,3,5,6],5)
    print(a.merge([1,2,3], 3, [0,0,0],0))
    # print([1,2,3,4,5,0,0,0][-3:])