class Solution:
    def reverseWords(self, s: str) -> str:
        # 过滤掉所有的空白元素
        tmp = [x for x in s.split(' ') if x != '']
        return ' '.join(tmp[::-1])


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("hello    world a!"))
