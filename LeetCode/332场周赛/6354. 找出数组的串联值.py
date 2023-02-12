nums = [5, 14, 13, 8, 12]

ret = 0
while len(nums) > 0:
    if len(nums) > 1:
        ret += int(str(nums[0]) + str(nums[-1]))
        nums = nums[1:-1]
    else:
        ret += int(nums[0])
        nums = []

print(ret)
    