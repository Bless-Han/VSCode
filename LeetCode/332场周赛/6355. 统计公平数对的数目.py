# 卡时间了
nums = [0,1,7,4,4,5]
lower = 3
upper = 6

ret = 0
l = len(nums)
for i1 in range(l):
    for i2 in range(i1 + 1, l):
        if lower <= nums[i1] + nums[i2] <= upper:
            ret += 1

# print(ret)
return ret
