class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, "", 1)
            else:
                return False
        return True
     # Create Counter objects for the ransomNote and magazine strings
        note, mag = Counter(ransomNote), Counter(magazine)
        
        # Check if the intersection of note and mag Counter objects is equal to note Counter object
        # If it is, it means that all the letters in ransomNote can be formed using the letters in magazine
        if note & mag == note: return True
        return False

a = "aa"
b = "aab"
s = Solution()
print(s.canConstruct(a, b))


a = "abcdefg"
a = a.replace("c","")
a
