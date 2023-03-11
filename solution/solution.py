class Solution:
    def findRepeatNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                print(nums)
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1

a, b, c = 1, 2, 3
a, b, c = c, a, b
print(a, b, c)
