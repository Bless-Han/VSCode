class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        aeiou = "aeiou"
        count = 0
        for word in words[left:right + 1]:
            if word[0] in aeiou and word[-1] in aeiou:
                count += 1
             
        return count


words = ["are","amy","u"]
s = Solution()
