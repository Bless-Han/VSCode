'''
   @pintia psid=994805260223102976 pid=994805277163896832 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1047 编程团体赛
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805277163896832
   
'''
# @pintia code=start
n = int(input())

for i in range(n):
    s = input().split()
    score = int(s[1])
    group = s[0].split("-")[0]
    if i == 0:
        all = {group: score}
    else:
        if group in all:
            all[group] += score
        else:
            all[group] = score

max_value = max()
print(max_group, max_score)



# @pintia code=end