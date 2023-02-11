'''
   @pintia psid=994805260223102976 pid=1071785664454127616 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1091 N-自守数
   
   https://pintia.cn/problem-sets/994805260223102976/problems/1071785664454127616
   
'''

# @pintia code=start
def main():
    m = input()
    numbers = input().split()
    numbers = map(int, numbers)
    for number in numbers:
        times = judge(number)
        if times != 0:
            print(times, times * number ** 2)
        else:
            print("No")

def judge(number):
    ret = 0
    
    l = len(str(number))
    super_number = number ** 2
    for i in range(10):
        if str(number) == str(super_number * i)[-l:]:
            return i
        
    return ret




main()
# @pintia code=end