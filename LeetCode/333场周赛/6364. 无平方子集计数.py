class Solution:
    def squareFreeSubsets(self, nums: list[int]) -> int:
        count = 0
        ziji = []
        quyu = 10 ** 9 + 7
        for num in nums:
            num %= quyu
            if (num ** 0.5 % 1 != 0 and num not in ziji) or num == 1:
                count += 1
                ziji.append(num)

        temp_ziji = ziji.copy()
        for i in range(len(temp_ziji)):
            for j in range(i + 1, len(temp_ziji)):
                temp = (temp_ziji[i] * temp_ziji[j]) % quyu
                if temp not in ziji and temp ** 0.5 % 1 != 0:
                    count += 1
                    ziji.append(temp)

        return count

    

s = Solution()
nums = [1]
print(s.squareFreeSubsets(nums))