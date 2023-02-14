'''
   @pintia psid=994805260223102976 pid=994805317546655744 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1007 素数对猜想
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805317546655744
   
'''

# @pintia code=start
def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())

pre = 2
count = 0
for i in range(3, n + 1):
    if is_prime(i):
        if i - pre == 2:
            count += 1
        pre = i
print(count)


# @pintia code=end