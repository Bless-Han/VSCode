class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        def change_to_dic(nums, dic):
            for num in nums:
                dic[num[0]] = num[1] if num[0] not in dic else dic[num[0]] + num[1]

        dic = {}
        change_to_dic(nums1, dic)
        change_to_dic(nums2, dic)
        nums3 = []
        for key in sorted(dic):
            nums3.append([key, dic[key]])
        return nums3




s = Solution()
nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]
print(s.mergeArrays(nums1, nums2))


