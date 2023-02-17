'''
   @pintia psid=994805260223102976 pid=994805289432236032 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1032 挖掘机技术哪家强
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805289432236032
   
'''
# @pintia code=start
# TODO before 102 ms
import sys
schools = {}
result_number = 0
result_score = 0

n = int(input())
for i in range(n):
    number, score = map(int, sys.stdin.readline().split())
    if i == 0:
        schools[number] = score
        result_number = number
        result_score = score
    else:
        if number in schools:
            schools[number] += score
        else:
            schools[number] = score
        
        if schools[number] > result_score:
            result_number = number
            result_score = schools[number]
            
print(result_number, result_score)

# @pintia code=end