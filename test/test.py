class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        ret = []
        l = len(nums)
        used = set()
        for i in range(l):
            min_j = i+1
            mn = abs(nums[i] - nums[j])
            for j in range(i+1, l):
                ...
            if i not in used and j not in used:
                used.add(i)
                used.add(j)
                ret.append(abs(nums[i]-nums[j]))
        if not p:
            return 0
        else:
            return max(sorted(ret)[:p])


print()
