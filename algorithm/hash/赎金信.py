# 本质就是判断第一个字符串所有的字符的数量都小于第二字符串当中的


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 每一个字符数量都要小于等于第二个字符串中的,时间复杂度高
        return all(ransomNote.count(c) <= magazine.count(c) for c in ransomNote)


class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}
        for c in magazine:
            counts[c] = counts.get(c, 0) + 1

        for c in ransomNote:
            # 没有出现的字符,或者字符已经用完了
            if c not in counts or counts[c] == 0:
                return False
            counts[c] -= 1

        return True


# 使用Counter
from collections import Counter


class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 两个Counter相减相当于是取差异,意思是ransomNote中存在但是magazine中不存在的字符的个数
        # 如果有差异,则相减的结果会是True(即结果中有值),我们所期望的应该是没有差异,结果不应该有值,所以使用not
        return not Counter(ransomNote) - Counter(magazine)
