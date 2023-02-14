'''
   @pintia psid=994805260223102976 pid=994805304020025344 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1018 锤子剪刀布
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805304020025344
   
'''

# @pintia code=start
# 根据对方的手势判断什么一直出什么手势将会赢
def will_win(x):
    min_shoushi = "B"
    min_count = x["B"]
    s = "C"
   
    

# return 1 a win, return -1 b win, return 0 no one win
def judge(a, b):
    max_shengsuan = {"J": "B", "B": "C", "C": "J"}
    ...



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

    
jia["will_win"] = will_win(yi)
yi["will_win"] = will_win(jia)

print(jia["sheng"], jia["ping"], jia["fu"])
print(yi["sheng"], yi["ping"], yi["fu"])
print(jia["will_win"], yi["will_win"])

# @pintia code=end