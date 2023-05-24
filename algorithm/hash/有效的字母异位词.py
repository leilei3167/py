class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = {}
        for i in s:
            # table[i]+=1 # 会报keyError
            table[i] = table.get(i, 0) + 1

        for l in t:
            table[l] = table.get(l, 0) - 1

        for k in table.keys():
            if table[k] != 0:
                return False

        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
