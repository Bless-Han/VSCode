'''
   @pintia psid=15 pid=2992 compiler=PYTHON3
   
   ProblemSet: 数据结构与算法题目集（中文）
   
   Title: 7-51 两个有序链表序列的合并
   
   https://pintia.cn/problem-sets/15/exam/problems/2992
   
'''
# @pintia code=start
a = list(map(int, input().split()))[:-1]
b = list(map(int, input().split()))[:-1]
c = sorted(a + b)
if len(c) == 0:
    print("NULL")
else:
    print(*c)

# @pintia code=end