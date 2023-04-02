class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        ret = []
        while nums:
            curr = []
            for n in nums:
                if n not in curr:
                    curr.append(n)
            ret.append(curr)
            # remove curr from nums
        return ret

nums = [1,3,4,1,2,3,1]
print(Solution().findMatrix(nums))
