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

e = a * c - b * d
f = a * d + b * c

e_str = "0.00" if e + 0.005 >= 0 and e < 0 else str(f"{e:.2f}")
if f + 0.005 >= 0 and f < 0:
    f_str = "+0.00"
elif f < 0:
    f_str = str(f"{f:.2f}")
else:
    f_str = str(f"+{f:.2f}")

print(e_str + f_str + "i")



# @pintia code=end
""" @pintia test=start
0.3 0.5 0.2 1.4
@pintia test=end """