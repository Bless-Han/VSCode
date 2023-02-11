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
    yinzi = []
    
    for i in range(1, int(number) + 1):
        if number % i == 0:
            yinzi.append(i)
    # print(yinzi)
    
    if len(yinzi) < 4:
        return False

    sums = []
    for i1, v1 in enumerate(yinzi):
        for i2, v2 in enumerate(yinzi[i1+1:]):
            for i3, v3 in enumerate(yinzi[i2+1:]):
                for i4, v4 in enumerate(yinzi[i3+1:]):
                    if number == v1 + v2 + v3 + v4:
                        # print(v1, v2, v3, v4, v1 + v2 + v3 + v4)
                        return True
                    # sums.append(v1 + v2 + v3 + v4)
    
    # print(sums)
    # for sm in sums:
    #     if number % sm == 0:
            # return True

    return False
    # TODO 去重
    # TODO 排序



main()
# @pintia code=end
""" @pintia test=start
1
36
@pintia test=end """