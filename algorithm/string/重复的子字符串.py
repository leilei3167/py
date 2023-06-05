class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return False

        next = self.get_next(s)

        # 关键点,最长前后缀不包含的部分就是重复子串,即数组的长度减去最长的前后缀;
        # 判断整个数组能否被这一部分整除即可
        if next[-1] != 0 and len(s) % (len(s) - next[-1]) == 0:
            return True
        return False

    def get_next(self, s):
        next = [0] * len(s)
        next[0] = 0
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

        return next
