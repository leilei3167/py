# 三数之和基础上再套一层循环
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        elif n == 4:
            return (
                [
                    nums,
                ]
                if sum(nums) == target
                else []
            )

        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if sum(nums[i : i + 4]) > target:
                break
            if nums[i] + sum(nums[n - 3 :]) < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + sum(nums[j : j + 3]) > target:
                    break
                if nums[i] + nums[j] + sum(nums[n - 2 :]) < target:
                    continue

                # 双指针模板写法
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res
