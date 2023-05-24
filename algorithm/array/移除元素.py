from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast, slow = 0, 0
        size = len(nums) - 1
        while fast <= size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


# 原地移除元素: 数组的元素在内存地址中是连续的，不能单独删除数组中的某个元素，只能覆盖


class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast, size = 0, 0, len(nums) - 1
        while fast <= size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow
