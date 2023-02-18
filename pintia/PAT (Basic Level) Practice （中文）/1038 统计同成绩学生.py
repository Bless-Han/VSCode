'''
   @pintia psid=994805260223102976 pid=994805284092887040 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1038 统计同成绩学生
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805284092887040
   
'''
# @pintia code=start
n = int(input())
scores = map(int, input().split())
lookup = list(map(int, input().split()[1:]))

count = []
for _ in range(101):
    count.append(0)

for score in scores:
    count[score] += 1
    
for i in range(len(lookup)):
    if i != 0:
        print(" ", end="")
    print(count[lookup[i]], end="")
print()


# @pintia code=end