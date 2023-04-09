class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return list(set(range(1, len(nums)+1)) - set(nums))


print()

set1 = {1, 2, 3}
set2 = [3, 4, 5]
set2.update(set1)
print(set2)
