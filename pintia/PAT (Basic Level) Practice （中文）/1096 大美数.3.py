'''
   @pintia psid=994805260223102976 pid=1478633632938655744 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1096 大美数
   
   https://pintia.cn/problem-sets/994805260223102976/problems/1478633632938655744
   
'''

# @pintia code=start
yinshu = [20]
def main():
    k = input()
    numbers = list(map(int, input().split()))
    for number in numbers:
        print("Yes") if is_dameishu(number) else print("No")
    

def is_dameishu(number):
    global yinshu
    yinshu = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            yinshu.append(i)
            if i ** 2 != number:
                yinshu.append(number / i)

    l = len(yinshu)
    for i1 in range(l):
        for i2 in range(i1 + 1, l):
            for i3 in range(i2 + 1, l):
                for i4 in range(i3 + 1, l):
                    if (yinshu[i1] + yinshu[i2] + yinshu[i3] + yinshu[i4]) % number == 0:
                        return True
    return False




main()
# @pintia code=end