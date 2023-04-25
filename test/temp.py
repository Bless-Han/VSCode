class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        d = {}
        for i in nums1:
            for j in nums2:
                if i+j in d:
                    d[i+j] += 1
                else:
                    d[i+j] = 1
        for i in nums3:
            for j in nums4:
                if -(i+j) in d:
                    count += d[-(i+j)]
        return count
    
    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    # Q: What's technique used here?
    # A: Hash table
