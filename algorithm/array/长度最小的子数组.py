from typing import List
import sys


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = sys.maxsize  # 定义一个无限大的数,记录最小的子数组长度
        Sum = 0  # 滑动窗口数值之和
        l = 0  # 滑动窗口起始位置
        for r in range(len(nums)):  # 右窗口指针一直右移,左指针的移动取决于窗口内值的和
            Sum += nums[r]
            while Sum >= s:
                res = min(res, r - l + 1)  # 比较当前结果和窗口大小,取较小值
                Sum -= nums[l]  # 移除最左边元素
                l += 1  # 窗口缩小(左指针右移)
        return 0 if res == sys.maxsize else res  # 如果res没有被赋值,说明没有符合条件的子数组,返回0
        # return (res, 0)[res == sys.maxsize]  # 如果res没有被赋值,说明没有符合条件的子数组,返回0


class Solution1:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = sys.maxsize
        total = 0
        l = 0
        # 右窗口是下标
        for i, v in enumerate(nums):
            total += nums[i]
            while total >= s:
                # 长度是右边界减左边界
                res = min(res, i - l + 1)
                # 左边界右移,移除该元素
                total -= nums[l]
                l += 1  # 缩小窗口
        return 0 if res == sys.maxsize else res
