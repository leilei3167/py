class Solution:
    def replaceSpace(self, s: str) -> str:
        ss = s.split(" ")
        return "%20".join(ss)

    def replaceSpace1(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if s[i] == ' ':
                res.append("%20")
            else:
                res.append(s[i])
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.replaceSpace("we are here"))
