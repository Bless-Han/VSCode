'''
   @pintia psid=994805260223102976 pid=994805300404535296 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1021 个位数统计
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805300404535296
   
'''

# @pintia code=start
n = input()
result = {}

for i in range(len(n)):
    number = int(n[i])
    result[number] = 1 if number not in result else: result[number] += 1
        
for key in sorted(result):
    print(key, result[key], sep=":")
        


# @pintia code=end