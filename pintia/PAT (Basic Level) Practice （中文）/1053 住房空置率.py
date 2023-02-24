'''
   @pintia psid=994805260223102976 pid=994805273284165632 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1053 住房空置率
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805273284165632
   
'''
# @pintia code=start
s = input().split()
n = int(s[0])
e = float(s[1])
d = int(s[2])

maybe = 0
sure = 0
for _ in range(n):
    less_then_e = 0
    temp = input().split()
    k = int(temp[0])
    dianliangs = list(map(float, temp[1:]))
    for x in dianliangs:
        less_then_e += 1 if x < e else 0
    if less_then_e > k / 2:
        if less_then_e > d:
            sure += 1
        else:
            maybe += 1

print(f"{(maybe / n * 100):.1f}% {(sure / n * 100):.1f}%")
        
    


# @pintia code=end
""" @pintia test=start
1 0.5 10
6 0.3 0.4 0.5 0.2 0.8 0.6
@pintia test=end """