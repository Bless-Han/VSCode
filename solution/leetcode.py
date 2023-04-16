class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans = {}
        for divisor in divisors:
            count = sum(1 for num in nums if num % divisor == 0)
            ans[divisor] = count
        max_divisor = divisors[0]
        max_count = 0
        print(ans)
        for k, v in ans.items():
            if v > max_count:
                max_count = v
                max_divisor = k
        return max_divisor
