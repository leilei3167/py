from typing import List


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        # 两两分组,得出相加的结果
        # nums1和nums2的结果
        m12 = {}
        for i1 in nums1:
            for i2 in nums2:
                if i1 + i2 in m12:
                    m12[i1 + i2] += 1
                else:
                    m12[i1 + i2] = 1
        count = 0
        for i3 in nums3:
            for i4 in nums4:
                # 找相反的结果
                need = -(i3 + i4)
                if need in m12:
                    count += m12[need]

        return count


from collections import defaultdict


class Solution1:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        m = defaultdict(lambda: 0)
        count = 0
        for i in nums1:
            for j in nums2:
                m[i + j] += 1
        for i in nums3:
            for j in nums4:
                count += m[-(i + j)]

        return count
