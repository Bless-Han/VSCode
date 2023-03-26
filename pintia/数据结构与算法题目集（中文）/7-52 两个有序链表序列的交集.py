'''
   @pintia psid=15 pid=2999 compiler=PYTHON3
   
   ProblemSet: 数据结构与算法题目集（中文）
   
   Title: 7-52 两个有序链表序列的交集
   
   https://pintia.cn/problem-sets/15/exam/problems/2999
   
'''
# @pintia code=start
a = input().split()[:-1]
b = input().split()[:-1]
c = []
for n in a:
    if n in b:
        c.append(n)
if len(c) == 0:
    print("NULL")
else:
    print(*c)

# @pintia code=end