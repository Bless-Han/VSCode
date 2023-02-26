class Solution:
    def leftRigthDifference(self, nums: list[int]) -> list[int]:
        def get_sum(numbers):
            ret = [0,]
            for number in numbers[: -1]:
                ret.append(ret[-1] + number)
            return ret

        left_sum = get_sum(nums)
        rigth_sum = get_sum(nums[::-1])[::-1]
        ret = []
        for i in range(len(left_sum)):
            ret.append(abs(left_sum[i] - rigth_sum[i]))

        return ret



nums = [10,4,8,3]
s = Solution()
print(s.leftRigthDifference(nums))
