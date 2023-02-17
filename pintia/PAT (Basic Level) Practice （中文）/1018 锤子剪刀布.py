'''
   @pintia psid=994805260223102976 pid=994805304020025344 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1018 锤子剪刀布
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805304020025344
   
'''
# @pintia code=start
# 返回赢次数最多的那一个手势
import sys

def win_max(x):
    ret = "B"
    for c in "CJ":
        if x[c] > x[ret]:
            ret = c

    return ret
    

# when ping return 0, win return 1, lose return 2
def judge(a, b):
    # 权值，用来判断输赢
    quanzhi = {"B": 0, "J": 1, "C": 2}
    return (quanzhi[a] - quanzhi[b]) % 3


# B C J 为各个手势赢的次数
jia = {"sheng": 0, "ping": 0, "fu": 0, "B": 0, "C": 0, "J": 0}
yi = {"B": 0, "C": 0, "J": 0}
n = int(input())
for i in range(n):
    a, b = sys.stdin.readline().split()
    match judge(a, b):
        case 1:
            jia["sheng"] += 1
            jia[a] += 1
            # yi["fu"] += 1
        case 0:
            jia["ping"] += 1
            # yi["ping"] += 1
        case 2:
            # yi["sheng"] += 1
            yi[b] += 1
            jia["fu"] += 1

print(jia["sheng"], jia["ping"], jia["fu"])
print(jia["fu"], jia["ping"], jia["sheng"])
print(win_max(jia), win_max(yi))

# @pintia code=end