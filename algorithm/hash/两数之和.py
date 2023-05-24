from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 以value:index的形式存入dict
        t = {}
        for i, v in enumerate(nums):
            need = target - v
            # 所需的值存在,获取其下标返回
            if need in t:
                return [i, t[need]]
            # 不存在,放入当前值
            t[v] = i

        return []


s = Solution()
s.twoSum([2, 7, 11, 15], 9)
