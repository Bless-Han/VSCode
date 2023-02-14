'''
   @pintia psid=994805260223102976 pid=994805309963354112 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1013 数素数
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805309963354112
   
'''

# @pintia code=start
def main():
    m, n = map(int, input().split())
    number = 2;
    primes = []
    for count in range(1, n + 1):
        while is_prime(number) == False:
            number += 1
        if m <= count <= n:
            primes.append(number)
        number += 1
            
    for i in range(0, len(primes), 10):
        print(*primes[i: i + 10])

def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


main()
# @pintia code=end