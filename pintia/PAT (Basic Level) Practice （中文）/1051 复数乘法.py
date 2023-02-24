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

x1, y1 = r1 * cos(p1), r1 * sin(p1)
x2, y2 = r2 * cos(p2), r2 * sin(p2)

a = round(x1 * x2 - y1 * y2 + 0.0001, 2)
b = round(x1 * y2 + y1 * x2 + 0.0001, 2)

result = ""
if a == 0:
    result += "0.00"
else:
    result += f"{a:.2f}"
    
if b == 0:
    result += "+0.00"
elif b < 0:
    result += f"{b:.2f}"
else:
    result += f"+{b:.2f}"

print(result + "i")


# @pintia code=end
""" @pintia test=start
0.3 0.5 0.2 0.4
@pintia test=end """