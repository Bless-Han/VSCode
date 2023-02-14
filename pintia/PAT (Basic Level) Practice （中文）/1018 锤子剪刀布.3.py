'''
   @pintia psid=994805260223102976 pid=994805304020025344 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1018 锤子剪刀布
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805304020025344
   
'''

# @pintia code=start
# 返回赢次数最多的那一个手势
def win_max(x):
    ret = "B"
    for c in "CJ":
        if x[c] > x[ret]:
            ret = c

    return ret
    

# return 1 a win, return -1 b win, return 0 no one win
def judge(a, b):
     = {"B": 0, "J": 1, "C": 2}



# B C J 为各个手势赢的次数
jia = {"sheng": 0, "ping": 0, "fu": 0, "B": 0, "C": 0, "J": 0}
yi = {"sheng": 0, "ping": 0, "fu": 0, "B": 0, "C": 0, "J": 0}
n = int(input())
for i in range(n):
    a, b = input().split()
    match judge(a, b):
        case -1:
            yi["sheng"] += 1
            jia["fu"] += 1
            yi[b] += 1
        case 0:
            yi["ping"] += 1
            jia["ping"] += 1
        case 1:
            yi["fu"] += 1
            jia["sheng"] += 1
            jia[a] += 1

print(jia["sheng"], jia["ping"], jia["fu"])
print(yi["sheng"], yi["ping"], yi["fu"])
print(win_max(jia), win_max(yi))

# @pintia code=end
""" @pintia test=start
10
C J
J B
C B
B B
B C
J C
J B
J B
B C
J J
@pintia test=end """
""" @pintia test=start
10
C J
J B
C B
B B
B C
C C
C B
J B
B C
J J
@pintia test=end """