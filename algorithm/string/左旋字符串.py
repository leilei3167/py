class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

    def reverseLeftWords1(self, s: str, n: int) -> str:
        # 前部分反转
        s = list(s)
        s[0:n] = list(reversed(s[0:n]))
        # 后部分反转再整体反转
        s[n:] = list(reversed(s[n:]))

        s.reverse()

        return "".join(s)
