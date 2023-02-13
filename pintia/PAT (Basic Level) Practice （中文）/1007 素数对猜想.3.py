'''
   @pintia psid=994805260223102976 pid=994805317546655744 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1007 素数对猜想
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805317546655744
   
'''

# @pintia code=start
def main():
    n = int(input())
    sushu = get_sushu(n)
    # 打印出差为2的素数
    print(count_dn2(sushu))


def get_sushu(n):
    ret = []
    for i in range(2, n):
        if is_sushu(i):
            ret.append(i)
    return ret


def is_sushu(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def count_dn2(sushu):
    ret = 0
    for i in range(len(sushu) - 1):
        if sushu[i+1] - sushu[i] == 2:
            ret += 1
    return ret



main()
# @pintia code=end