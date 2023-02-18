'''
   @pintia psid=994805260223102976 pid=994805280817135616 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1042 字符统计
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805280817135616
   
'''
# @pintia code=start
s = input().lower()

al_count = {}
for c in s:
    if c.isalpha():
        if c not in al_count:
            al_count[c] = 1
        else:
            al_count[c] += 1

# 找到出现最多的那个字母
result_key = ""
for key in sorted(al_count):
    if result_key not in al_count:
        result_key = key
    elif al_count[key] > al_count[result_key]:
        result_key = key

print(result_key, al_count[result_key])



# @pintia code=end