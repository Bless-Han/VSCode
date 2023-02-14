'''
   @pintia psid=994805260223102976 pid=994805304020025344 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1018 锤子剪刀布
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805304020025344
   
'''

# @pintia code=start
# 根据 x 的手势判断什么一直出什么手势将会赢过 x
def will_win(x):
    max_shengsuan = {"J": "B", "B": "C", "C": "J"}
    # 胜率
    shenglv = {"B": 0, "C": 0, "J": 0}
    ret = "B"
    for key in shenglv:
        

    return ret
   
    

# return 1 a win, return -1 b win, return 0 no one win
def judge(a, b):
    if a == b:
        return 0
    elif (a == "J" and b == "B") or (a == "B" and b == "C") or (a == "C" and b == "J"):
        return 1
    else:
        return -1



# will_win 是最有可能胜的手势
jia = {"sheng": 0, "ping": 0, "fu": 0, "B": 0, "C": 0, "J": 0, "will_win": "B"}
yi = {"sheng": 0, "ping": 0, "fu": 0, "B": 0, "C": 0, "J": 0, "will_win": "B"}
n = int(input())
for i in range(n):
    a, b = input().split()
    jia[a] += 1
    yi[a] += 1
    match judge(a, b):
        case -1:
            yi["sheng"] += 1
            jia["fu"] += 1
        case 0:
            yi["ping"] += 1
            jia["ping"] += 1
        case 1:
            yi["fu"] += 1
            jia["sheng"] += 1

print(jia["sheng"], jia["ping"], jia["fu"])
print(yi["sheng"], yi["ping"], yi["fu"])
print(will_win(yi), will_win(jia))

# @pintia code=end