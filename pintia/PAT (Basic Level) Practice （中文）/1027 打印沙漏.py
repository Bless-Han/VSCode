'''
   @pintia psid=994805260223102976 pid=994805294251491328 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1027 打印沙漏
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805294251491328
   
'''
# @pintia code=start
n, c = input().split()
n = int(n)

rows = 0
while rows * rows * 2 - 1 <= n:
    rows += 1
rows -= 1

rest = n - (rows * rows * 2 - 1)

current_row = rows
while current_row > 1:
    print(" " * (rows - current_row) + c * (current_row * 2 - 1))
    current_row -= 1
while current_row <= rows:
    print(" " * (rows - current_row) + c * (current_row * 2 - 1))
    current_row += 1
    
print(rest)



# @pintia code=end
""" @pintia test=start
1 $
@pintia test=end """