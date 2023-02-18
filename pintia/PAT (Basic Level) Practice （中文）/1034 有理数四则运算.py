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


def huajian(k):
    ret = ""
    k1, k2 = map(int, k.split("/"))
    
    # get sign
    if k1 < 0:
        sign = "-"
        k1 *= -1
    else:
        sign = "+"

    # get 整数部分
    zhengshu = k1 // k2
    k1 %= k2
    
    if k1 > 0:
        if zhengshu > 0:
            ret += str(zhengshu)
            ret += " "
        zdgys = zdgy(k1, k2)
        k1 //= zdgys
        k2 //= zdgys
        ret += str(k1) + "/" + str(k2)
    elif zhengshu == 0:
        return "0"
    else:
        ret += str(zhengshu)
        

    if sign == "-":
        ret = "(-" + ret + ")"

    return ret


def plus(a, b):
    c1 = a1 * b2 + b1 * a2
    c2 = a2 * b2
    c = str(c1) + "/" + str(c2)
    return huajian(a) + " + " + huajian(b) + " = " + huajian(c)


def minus(a, b):
    c1 = a1 * b2 - b1 * a2
    c2 = a2 * b2
    c = str(c1) + "/" + str(c2)
    return huajian(a) + " - " + huajian(b) + " = " + huajian(c)


def times(a, b):
    c1 = a1 * b1
    c2 = a2 * b2
    c = str(c1) + "/" + str(c2)
    return huajian(a) + " * " + huajian(b) + " = " + huajian(c)


def division(a, b):
    ret = ""
    b2 = ""
    if b2 == "0":
        ret = "Inf"
    else:
        ...
    return ret
    

a, b = input().split()
a1, a2 = map(int, a.split("/"))
b1, b2 = map(int, b.split("/"))
print(plus(a, b))
print(minus(a, b))
print(times(a, b))
print(division(a, b))


# @pintia code=end