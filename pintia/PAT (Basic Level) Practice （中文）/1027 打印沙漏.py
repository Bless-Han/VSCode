'''
   @pintia psid=994805260223102976 pid=994805294251491328 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1027 打印沙漏
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805294251491328
   
'''
# @pintia code=start
n, c = input().split()
n = int(n)
row = 1
while (2 * row * row - 1) <= n:
    row += 1
row -= 1
count = n - (2 * row * row - 1)
for i in range(2 * row - 1, 0, -2):
    print(" " * ((2 * row - 1 - i) // 2), end="")
    print(c * i)
for i in range(3, 2 * row, 2):
    print(" " * ((2 * row - 1 - i) // 2), end="")
    print(c * i)
print(count)




# @pintia code=end
""" @pintia test=start
6 $
@pintia test=end """