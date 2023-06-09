from typing import List


# 数组是有序的,数组平方最大值一定在两端,取两端指针,比较平方大小,较大的放入新数组最右边
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, n = 0, len(nums) - 1, len(nums) - 1
        res = [0] * len(nums)  # 创建一个长度为len且所有元素都为0的列表
        while l <= r:
            lm = nums[l] ** 2
            rm = nums[r] ** 2
            if lm > rm:
                res[n] = lm
                l += 1  # 左指针右移
            else:
                res[n] = rm
                r -= 1
            n -= 1  # 新数组指针左移
        return res


# 暴力解法,平方后排序
class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i**2 for i in nums])


# 双指针
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, n = 0, len(nums) - 1, len(nums) - 1
        new_list = [0] * len(nums)  # 新列表容纳结果
        while l <= r:
            lm = nums[l] ** 2
            rm = nums[r] ** 2
            if lm > rm:
                new_list[n] = lm
                l += 1
            else:
                new_list[n] = rm
                r -= 1

            n -= 1
        return new_list
