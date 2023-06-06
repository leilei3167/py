from typing import List


class MyQueue:  # 单调队列（从大到小
    def __init__(self):
        from collections import deque
        self.queue = deque()  # 这里需要使用deque实现单调队列，直接使用list会超时

    # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    # 同时pop之前判断队列当前是否为空。
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()  # list.pop()时间复杂度为O(n),这里需要使用collections.deque()

    # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    # 这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    # 查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
    def front(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []
        # 第一个窗口:
        for i in range(k):  # 先将前k的元素放进队列
            que.push(nums[i])
        result.append(que.front())  # 第一个窗口的最大值

        # 窗口开始移动
        for i in range(k, len(nums)):
            # 新的窗口实际上相对于上一个窗口少了一个左边元素,多了一个右边元素
            que.pop(nums[i - k])  # 滑动窗口左边界右移
            que.push(nums[i])  # 滑动窗口前加入最后面的元素
            result.append(que.front())  # 记录对应的最大值
        return result

    # def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
    #     """暴力解法,会超时"""
    #     index_l = 0
    #     index_r = index_l + k
    #     biggest = []
    #     while index_r <= len(nums):
    #         biggest.append(max([nums[i] for i in range(index_l, index_r)]))
    #         index_l += 1
    #         index_r += 1
    #     return biggest


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
