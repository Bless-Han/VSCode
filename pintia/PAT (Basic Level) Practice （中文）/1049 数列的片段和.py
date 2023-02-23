'''
   @pintia psid=994805260223102976 pid=994805275792359424 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1049 数列的片段和
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805275792359424
   
'''
# @pintia code=start
import sys
aaaaaaa = input()
numbers = list(map(float, sys.stdin.readline().split()))
result = 0

# 临时计算
temp_a = 0
# 求一个数的总
sum_a_number = 0
for i in range(len(numbers)):
    temp_a += numbers[i]
    sum_a_number += temp_a

for i in range(len(numbers)):
    if i == 0:
        result += sum_a_number
        continue
    # TODO


    

print(f"{result:.02f}")


# @pintia code=end
""" @pintia test=start
3
1 2 3
@pintia test=end """