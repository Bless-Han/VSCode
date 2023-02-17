'''
   @pintia psid=994805260223102976 pid=994805289432236032 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1032 挖掘机技术哪家强
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805289432236032
   
'''
# @pintia code=start
import sys
schools = []
result_number = 0
result_score = 0

for i in range(100000 + 2):
    schools.append(0)

n = int(input())
for i in range(n):
    number, score = map(int, sys.stdin.readline().split())
    schools[number] += score
    if schools[number] > result_score:
        result_number = number
        result_score = schools[number]
            
print(result_number, result_score)

# @pintia code=end