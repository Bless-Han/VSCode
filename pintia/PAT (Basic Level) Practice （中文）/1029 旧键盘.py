'''
   @pintia psid=994805260223102976 pid=994805292322111488 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1029 旧键盘
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805292322111488
   
'''
# @pintia code=start
s1 = input().upper()
s2 = input().upper()
result = ""
for c in s1:
    if c not in s2 and c not in result:
        result += c

print(result)

# @pintia code=end