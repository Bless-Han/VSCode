class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def count(s):
            ret = {}
            for c in s:
                ret[c] = 1 if c not in ret else ret[c] + 1
            return ret
        
        ranCount = count(ransomNote)
        magCount = count(magazine)
        if ranCount & magCount == ranCount:
            return True
        else:
            return False

a = "aa"
b = "aab"
s = Solution()
print(s.canConstruct(a, b))


a = "abcdefg"
a = a.replace("c","")
a
