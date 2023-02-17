'''
   @pintia psid=994805260223102976 pid=994805294251491328 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1027 打印沙漏
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805294251491328
   
'''
# @pintia code=start
n, c = input().split()
n = int(n)
# 计算一半的高度
height = 1
stars = 1
while stars <= n:
    height += 1
    stars += ((height * 2) - 1) * 2
height -= 1




# @pintia code=end
""" @pintia test=start
3 $
@pintia test=end """