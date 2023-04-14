class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index = 0
        max_other = 0
        for i in range(len(nums)):
            if nums[i] > nums[max_index]:
                max_other = nums[max_index]
                max_index = i
        if max_other * 2 > nums[max_index]:
            return -1
        else:
            return max_index

