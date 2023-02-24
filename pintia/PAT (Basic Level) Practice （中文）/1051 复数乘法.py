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
a, b = change(r1, p1)
c, d = change(r2, p2)

e = round(a * c - b * d + 0.0001, 2)
f = round(a * d + b * c + 0.0001, 2)

result = ""
result = "0.00" if e == 0 else str(f'{e:.2f}')
if f == 0:
    result += "+0.00"
elif f < 0:
    result += str(f'{f:.2f}')
else:
    result += str(f'+{f:.2f}')

print(result + "i")



# @pintia code=end
""" @pintia test=start
0.3 0.5 0.2 1.4
@pintia test=end """