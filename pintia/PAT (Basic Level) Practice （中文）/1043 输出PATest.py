'''
   @pintia psid=994805260223102976 pid=994805280074743808 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1043 输出PATest
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805280074743808
   
'''
# @pintia code=start
def print_pat(count):
    for key in count:
        if count[key] > 0:
            print(key, end="")
            count[key] -= 1
    
    
s = input()

# count: 统计"PATest"各个字符出现的次数计数
count = {}
# 初始化
for c in "PATest":
    count[c] = 0
for c in s:
    if c in count:
        count[c] += 1

# max: 最终打印循环的次数
max = 0
for c in count:
    if count[c] > max:
        max = count[c]

for _ in range(max):
    print_pat(count)
print()

# @pintia code=end