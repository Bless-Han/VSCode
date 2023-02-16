'''
   @pintia psid=994805260223102976 pid=994805298269634560 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1023 组个最小数
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805298269634560
   
'''

# @pintia code=start
# 打印非0的最小数，并且更新数组
numbers = list(map(int, input().split()))

result = ""
for i in range(1, len(numbers)):
    if numbers[i] > 0:
        result += str(i)
        numbers[i] -= 1
        break

for i in range(len(numbers)):
    result += str(i) * numbers[i]
# 
print(result)



# @pintia code=end