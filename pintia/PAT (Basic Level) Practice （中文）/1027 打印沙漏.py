'''
   @pintia psid=994805260223102976 pid=994805294251491328 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1027 打印沙漏
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805294251491328
   
'''
# @pintia code=start
n, c = input().split()
n = int(n)

height = 1
stars = 1
while stars <= n:
    height += 1
    stars += (height * 2 - 1) * 2
height -= 1

current_height = height
# judge: 过半变-1
judge = 1
while True:
    # 到中点
    if current_height == 1:
        judge = -1

    current_stars = current_height * 2 - 1
    print(" " * (height - current_height) + c * current_stars)

    n -= current_stars
    if current_height == height and judge == -1:
        print(n)
        break

    current_height -= judge

# @pintia code=end
""" @pintia test=start
6 $
@pintia test=end """