'''
   @pintia psid=994805260223102976 pid=994805274496319488 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1051 复数乘法
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805274496319488
   
'''
# @pintia code=start
from math import cos
from math import sin


def change(r, p):
    return r * cos(p), r * sin(p)


r1, p1, r2, p2 = map(float, input().split())

a, b = change(r1, p1)
c, d = change(r2, p2)

r = round(a * c - b * d + 0.0001, 2)
i = round(a * d + b * c + 0.0001, 2)

result = ""
if r == 0:
    result += "0.00"
else:
    result += str(r)

if i == 0:
    result += "+0.00"
elif i > 0:
    result += "+" + str(i)
else:
    result += str(i)

print(result + "i")


# @pintia code=end
""" @pintia test=start
0.3 0.5 0.2 0.0004
@pintia test=end """