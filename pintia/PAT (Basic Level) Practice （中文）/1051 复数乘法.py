'''
   @pintia psid=994805260223102976 pid=994805274496319488 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1051 复数乘法
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805274496319488
   
'''
# @pintia code=start
from math import cos
from math import sin


r1, p1, r2, p2 = map(float, input().split())
a1, b1 = r1 * cos(p1), r1 * sin(p1)
a2, b2 = r2 * cos(p2), r2 * sin(p2)

a3 = round(a1 * a2 - b1 * b2 + 0.0001, 2)
b3 = round(a1 * b2 + b1 * a2 + 0.0001, 2)

result = ""
if a3 == 0:
    result += "0.00"
else:
    result += f"{a3:.2f}"
if b3 == 0:
    result += "+0.00i"
elif b3 > 0:
    result += f"+{b3:.2f}i"
else:
    result += f"{b3:.2f}i"

print(result)


# @pintia code=end
""" @pintia test=start
0.3 0.5 0.2 0.4
@pintia test=end """