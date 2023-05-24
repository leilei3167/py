class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            # 转换为字符串后依次遍历,再转换为整数计算平方,6!
            n = sum([int(i) ** 2 for i in str(n)])
            if n in seen:
                return False
            seen.add(n)
        return True
