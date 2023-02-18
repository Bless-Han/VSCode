class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(ans, s, left, right):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                backtrack(ans, s + "(", left + 1, right)
            if right < left:
                backtrack(ans, s + ")", left, right + 1)
            
        ans = []
        backtrack(ans, "", 0, 0)
        return ans
    

s = Solution()