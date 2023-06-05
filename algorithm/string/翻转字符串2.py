class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        index = 0
        while index < len(s):
            # 这部分需要翻转
            cur = index + k
            s = s[:index] + s[index:cur][::-1] + s[cur:]
            # 每次步长2k
            index = index + 2 * k
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr("abcdefg", 2))
