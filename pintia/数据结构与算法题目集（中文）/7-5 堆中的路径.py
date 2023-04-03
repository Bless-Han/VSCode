'''
   @pintia psid=15 pid=713 compiler=PYTHON3
   
   ProblemSet: 数据结构与算法题目集（中文）
   
   Title: 7-5 堆中的路径
   
   https://pintia.cn/problem-sets/15/exam/problems/713
   
'''
# @pintia code=start
N, M = map(int, input().split())
# Q: Why 0 in the head of H?
# A: Because the index of H starts from 1.
# Q: starts from 0 and from 1. which is better?
# A: starts from 1 is better.
# Q: why?
# A: Because the index of H starts from 1.
# Q: Thank you.
# A: You are welcome.
for num in nums:
    H.append(num)
    i = len(H) - 1
    while i > 1:
        if H[i] < H[i // 2]:
            H[i], H[i // 2] = H[i // 2], H[i]
            i = i // 2
        else:
            break
for i in map(int, input().split()):
    path = []
    while i > 0:
        path.append(H[i])
        i = i // 2
    print(*path)




# @pintia code=end