class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
# Q: Why t[i] in d.values() then return False?
# A: Because if t[i] in d.values(), it means that t[i] has been mapped to another s[i] before.
# Q: I know now, because of the precondition "No two characters may map to the same character, but a character may map to itself." Thank you.
# A: You are welcome.
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False
        return True