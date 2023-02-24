'''
   @pintia psid=994805260223102976 pid=994805274496319488 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1051 复数乘法
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805274496319488
   
'''
# @pintia code=start
import math


def change(r, p):
    return r * math.cos(p), r * math.sin(p)


r1, p1, r2, p2 = map(float, input().split())
a, b = change(r1, p2)
c, d = change(r2, p2)
print(a, b, c, d)

e = round(a * c - b * d + 0.00001, 2)
f = round(a * d + b * c + 0.00001, 2)

print(f"{e}{f}i")


# @pintia code=end