'''
   @pintia psid=994805260223102976 pid=994805299301433344 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1022 D进制的A+B
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805299301433344
   
'''

# @pintia code=start
s = input().split()
a, b, d = map(int, s)
sum = a + b
result = ""
while sum != 0:
    result = str(sum % d) + result
    sum //= d

if result == "":
    print("0")
else:
    print(result)



# @pintia code=end