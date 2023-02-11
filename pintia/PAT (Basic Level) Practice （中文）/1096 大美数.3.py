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
    sums = get_sums(number)

    for sm in sums:
        if number % sm == 0:
            return True
    
    return False


def get_sums(number):
    yinzi = []
    
    for i in range(number / 2 + 1):
        if number % i == 0:
            yinzi.append(i)

    sums = []
    for x in yinzi:

        
    # TODO 去重
    # TODO 排序



main()
# @pintia code=end