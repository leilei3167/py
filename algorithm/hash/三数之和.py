from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 因为不可重复,使用双指针,必须先对其从小到大排序
        nums.sort()
        result = []
        for i in range(len(nums)):
            # 如果最小的元素都大于零了,肯定是没结果
            if nums[i] > 0:
                return result

            # 跳过相同的元素避免重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 左指针
            left = i + 1
            # 右指针
            right = len(nums) - 1

            while right > left:
                sum_ = nums[i] + nums[left] + nums[right]

                # 判断大小
                # 小了,左指针应该右移
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    # 大了,右边左移
                    right -= 1
                else:
                    # 构建三元组
                    result.append([nums[i], nums[left], nums[right]])

                    # 移动到最后一个和右指针相等的元素位置
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    # 移动到最后一个和左指针相等的元素位置
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1

                    # 移动
                    right -= 1
                    left += 1
        return result
