'''
   @pintia psid=994805260223102976 pid=994805317546655744 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1007 素数对猜想
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805317546655744
   
'''

# @pintia code=start
import math
def main():
    n = int(input())
    pre = 2
    count = 0
    for i in range(3, n + 1, 2):
        if is_prime(i) == 1:
            if i - pre == 2:
                count += 1
            pre = i
        
    print(count)


def is_prime(x):
    if x < 2:
        return False
    sqr = int(math.sqrt(x))
    for i in range(2, sqr + 1):
        if x % i == 0:
            return False
    return True


main()
# @pintia code=end