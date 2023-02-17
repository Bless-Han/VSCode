'''
   @pintia psid=994805260223102976 pid=994805294251491328 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1027 打印沙漏
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805294251491328
   
'''
# @pintia code=start
n, c = input().split()
n = int(n)

# 计算出预计使用的层数
floor = 1
# 计划使用星星的数量
stars = 0
while stars < n:
    floor += 1
    stars += (floor * 2 - 1) * 2
floor -= 1

# 用来增加或者减少空格和字符的数量。过中点之后变为-1
change = 1
# 当前层数
current_floor = floor
while True:
    # 将要使用字符的数量
    will_use = current_floor * 2 - 1
    if n > will_use:
        n -= will_use
        print(" " * (floor - current_floor), will_use * c, sep="")
        if will_use == 1:
            change *= -1

        current_floor -= change
    elif n > 0:
        print(n)
        break
    else:
        break

    


# @pintia code=end
""" @pintia test=start
12 $
@pintia test=end """