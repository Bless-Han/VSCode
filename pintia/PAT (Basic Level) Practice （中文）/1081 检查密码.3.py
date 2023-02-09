'''
   @pintia psid=994805260223102976 pid=994805261217153024 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1081 检查密码
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805261217153024
   
'''

# @pintia code=start
# TODO 判断字符串是否仅由数字和字母组成
# 0: wanmei, 1: duan, 2: luan, 3: need number, 4:need zimu
dic = {
    0: "Your password is wan mei.",
    1: "Your password is tai duan le.",
    2: "Your password is tai luan le.",
    3: "Your password needs shu zi.",
    4: "Your password needs zi mu.",
}

def main():
    n = int(input())
    for i in range(n):
        s = input()
        print(dic(judge(s)))


# judge a str and return a number
def judge(s):        
    if len(s) <= 6:
        return 1
    
    return 0



main()
# @pintia code=end