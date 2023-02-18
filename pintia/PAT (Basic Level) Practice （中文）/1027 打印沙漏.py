'''
   @pintia psid=994805260223102976 pid=994805294251491328 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1027 打印沙漏
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805294251491328
   
'''
# @pintia code=start
n, c = input().split()
n = int(n)
num = 1
while (2*num-1)**2-2*num+1 <= n:
    num += 1
num -= 1
used = (2*num-1)**2-2*num+1

for i in range(2*num-1, 0, -2):
    s = (2*num-1-i)//2
    print(' ' * s + c * i)

for i in range(3, 2*num+1, 2):
    s = (2*num-i)//2
    print(' ' * s + c * i)

print(n - used)




# @pintia code=end
""" @pintia test=start
6 $
@pintia test=end """