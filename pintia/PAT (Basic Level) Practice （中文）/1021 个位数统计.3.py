'''
   @pintia psid=994805260223102976 pid=994805300404535296 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1021 个位数统计
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805300404535296
   
'''

# @pintia code=start
n = input()

# creat a dictionary
result = {}

# TODO add key and value to result
for i in range(10):
    number = n.count(str(i))
    if number > 0:
        result[i] = number


# TODO print result
for key in result:
    print(key, result[key], sep=":")


# @pintia code=end