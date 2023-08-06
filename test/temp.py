
nums = list(map(int, input().split()))
for i in range(1, len(nums)):
    if nums[i] > 0:
        print(i, end="")
        nums[i] -= 1
        break
    
for i in range(len(nums)):
    while nums[i]:
        print(i, end="")
        nums[i] -= 1
        
print()