import re
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCount = {}
        for c in magazine:
            magCount[c] = 1 if c not in magCount else magCount[c] + 1
        for c in ransomNote:
            if c not in magCount:
                return False
            else:
                magCount[c] -= 1
            if magCount[c] < 0:
                return False
        return True

60 * 0.83


a = 9
print(f"{a:02}")
