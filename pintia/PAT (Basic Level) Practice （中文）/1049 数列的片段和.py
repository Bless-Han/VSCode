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

for i in range(len(numbers)):
    tmp = 0
    for j in range(i, len(numbers)):
        tmp += numbers[j]
        result += tmp

print(f"{result:.02f}")


# @pintia code=end