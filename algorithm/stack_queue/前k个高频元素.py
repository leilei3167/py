import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """实际上应该使用优先级队列(堆),采用小顶堆,这样就只需要维护k个元素,nlogk的时间复杂度"""
        map_ = {}
        for i in nums:
            map_[i] = map_.get(i, 0) + 1

        # 构建小顶堆
        pri_que = []
        # 用固定大小为k的小顶堆
        for item, freq in map_.items():
            # 存入的数据是一个元组,为出现的频率和对应的k
            heapq.heappush(pri_que, (freq, item))
            # 只维护k个大小的堆,超过了就弹出
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        # 弹出数值,因为是从根节点弹出,而根节点又是最小的值,所以要按倒序输出
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        cnt = Counter(nums)
        # 以数量从大到小排序
        tmp = sorted(cnt.items(), key=lambda a: a[1], reverse=True)
        return [i[0] for i in tmp][:k]

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        # 统计出现次数
        tmp = {}
        for i in nums:
            tmp[i] = tmp.get(i, 0) + 1
        res = []
        for i in tmp.keys():
            res.append(i)

        # 排序
        return sorted(res, key=lambda x: tmp[x], reverse=True)[:k]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
