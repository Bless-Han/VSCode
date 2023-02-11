'''
   @pintia psid=994805260223102976 pid=1478633632938655744 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1096 大美数
   
   https://pintia.cn/problem-sets/994805260223102976/problems/1478633632938655744
   
'''

# @pintia code=start
def main():
    k = input()
    numbers = input().split()
    numbers = map(int, numbers)

    for number in numbers:
        if judge(number) == True:
            print("Yes")
        else:
            print("No")


def judge(number):
    ...



main()
# @pintia code=end
""" @pintia test=start
1
900
@pintia test=end """