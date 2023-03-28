'''
   @pintia psid=15 pid=709 compiler=PYTHON3
   
   ProblemSet: 数据结构与算法题目集（中文）
   
   Title: 7-1 最大子列和问题
   
   https://pintia.cn/problem-sets/15/exam/problems/709
   
'''
# @pintia code=start
k = input()
numbers = list(map(int, input().split()))
curr = 0
max = 0
for n in numbers:
    curr += n
    if curr > max:
        max = curr
    if curr < 0:
        curr = 0
print(max)



# @pintia code=end