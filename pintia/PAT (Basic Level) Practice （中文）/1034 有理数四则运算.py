'''
   @pintia psid=994805260223102976 pid=994805287624491008 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1034 有理数四则运算
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805287624491008
   
'''
# @pintia code=start
# 求两个数的最大公约数
def zdgy(a, b):
    a = abs(a)
    b = abs(b)
    while a % b != 0:
        c = a % b
        a = b
        b = c
    return b


def minus(a, b):
    ...


def plus(a, b):
    ...


def times(a, b):
    ...


def division(a, b):
    ...
    

a, b = input().split()



# @pintia code=end