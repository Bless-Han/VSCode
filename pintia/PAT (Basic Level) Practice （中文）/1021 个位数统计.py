'''
   @pintia psid=994805260223102976 pid=994805300404535296 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1021 个位数统计
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805300404535296
   
'''
# @pintia code=start
dic = {}
for i in range(10):
    dic[str(i)] = 0

n = input()
for c in n:
    dic[c] += 1

for key, value in dic.items():
    if value > 0:
        print(f"{key}:{value}")



# @pintia code=end