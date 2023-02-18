'''
   @pintia psid=994805260223102976 pid=994805284923359232 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1037 在霍格沃茨找零钱
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805284923359232
   
'''
# @pintia code=start
# 将零钱兑换成大票 返回字符串
def duihuan(money):
    if money < 0:
        sign = "-"
        money *= -1
    else:
        sign = ""

    ret1 = ""
    ret2 = ""
    ret3 = money
    
    # from money to ret3 and ret2
    if ret3 > 0:
        ret2 = ret3 // 29
        ret3 %= 29
    
    if ret2 != "":
        ret1 = ret2 // 17
        ret2 %= 17
    
    ret3 = str(ret3)
    ret2 = ret2 + "." if ret2 != "" else ""
    ret3 = ret3 + "." if ret3 != "" else ""
    
    return sign + ret1 + ret2 + ret3


p, a = input().split()
p1, p2, p3 = map(int, p.split("."))
a1, a2, a3 = map(int, a.split("."))

should_pay = (p1 * 17 + p2) * 29 + p3
real_pay = (a1 * 17 + a2) * 29 + a3

change = real_pay - should_pay

ret = "-" if change < 0 else ""

print(duihuan(change).strip("."))

# @pintia code=end