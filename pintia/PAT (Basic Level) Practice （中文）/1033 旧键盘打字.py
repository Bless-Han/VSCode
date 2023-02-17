'''
   @pintia psid=994805260223102976 pid=994805288530460672 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1033 旧键盘打字
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805288530460672
   
'''
# @pintia code=start
shift_broken = False
s1 = input().upper()
s2 = input()

if "+" in s1:
    shift_broken = True

result = ""
for c in s2:
    if shift_broken == True and c.isupper():
        continue
    if c.upper() in s1:
        continue
    result += c
    
print(result)

# @pintia code=end