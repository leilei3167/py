class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """kmp算法经典题
        KMP的主要思想是当出现字符串不匹配时，可以知道一部分之前已经匹配的文本内容，可以利用这些信息避免从头再去做匹配了
        核心是如何构建next数组(前缀表)
        前缀表是用来回退的,记录的是当模式串与文本串不匹配的时候,模式串应该回退到哪个位置继续匹配
        前缀表就是记录下标i之前（包括i）的字符串中，有多大长度的相同前缀后缀:最长公共前后缀

        前缀表要求的就是相同前后缀的最大长度
        前缀是指以第一个字符开头,除最后一个字符外的所有连续子串
        后缀是指不包含第一个字符的所有一最后一个字符结尾的所有连续子串
        如:
        a 为0,没有前后缀
        aa 为1,前缀为a,后缀为a
        aaa 为2,前缀为a,aa,后缀aa,a
        aaaa 为3,前缀为a,aa,aaa后缀为aaa,aa,a
        ab 为0
        aab 为0
        aaba 为1 前缀a,aa,aab,后缀aba,ba,a因此为1
        aabaa 前缀为a,aa,aab,aaba,后缀为abaa,baa,aa,因此最长公共前后缀值为2

        前缀表就是记录下标i之前（包括i）的字符串中，有多大长度的相同前缀后缀:最长公共前后缀,如
        aabaaf模式串有如下表示:
        索引: 0 1 2 3 4 5
        元素: a a b a a f
        值 :  0 1 0 1 2 0
        就能够表示索引(i)或之前的字符串中,其最大长度的相同前后缀的是多少,
        如i=4处的字符串有长度为2的最大长度的相同前后缀

        当进行到不匹配的位置时,根据前缀表当前元素的前一位(这个值就是应该回退的模式串的索引处)

        """
        if len(needle) == 0:
            return 0

        # 将模式串构建next数组
        next = self.get_next(needle)
        j = 0  # 已匹配的长度
        # 和文本串进行匹配
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]  # 前缀表不匹配元素的前一个值就是应该回退的字符串索引
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1

    def get_next(self, needle):
        next = [0] * len(needle)
        # 第一位因为是单字符所以一定是0
        next[0] = 0
        # j用来记录前缀的末尾位置,i指向后缀末尾位置
        j = 0
        for i in range(1, len(needle)):
            # j最小就为0,当j不为0,进入此处说明前后缀就不同了,需要回退
            while j > 0 and needle[i] != needle[j]:
                j = next[j - 1]  # 这一个位置不匹配,找前一位对应的回退位置
            if needle[i] == needle[j]:
                j += 1  # 匹配,长度+1
            next[i] = j
        return next

    def strStr1(self, haystack, needle):
        """
        暴力法
        """

        m, n = len(haystack), len(needle)
        # 从主串截取
        for i in range(m):
            if haystack[i:i + n] == needle:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("hello", "ll"))
