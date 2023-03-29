'''
   @pintia psid=15 pid=721 compiler=PYTHON3
   
   ProblemSet: 数据结构与算法题目集（中文）
   
   Title: 7-13 统计工龄
   
   https://pintia.cn/problem-sets/15/exam/problems/721
   
'''
# @pintia code=start
n = input()
people = map(int, input().split())
dic = {}
for p in people:
    dic[p] = 1 if p not in dic else dic[p] + 1

for d in sorted(dic):
    print(f"{d}:{dic[d]}")

# @pintia code=end
""" @pintia test=start
8
10 2 0 5 7 2 5 2

@pintia test=end """