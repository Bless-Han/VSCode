'''
   @pintia psid=994805260223102976 pid=994805276438282240 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1048 数字加密
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805276438282240
   
'''
# @pintia code=start
def change(a, b):
    ret = ""
    if len(b) > len(a):
        ret += b[len(a): ]
    b_l = len(b)
    for i in range(b_l):
        if (b_l - i) % 2 == 0:
            # 取余13后的数字
            # TODO 
        else:
            ...
    
a, b = input().split()
a = a[::-1]
b = b[::-1]

print(change(a, b))

# @pintia code=end