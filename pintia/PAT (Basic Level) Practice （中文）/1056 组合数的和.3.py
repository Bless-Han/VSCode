'''
   @pintia psid=994805260223102976 pid=994805271455449088 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1056 组合数的和
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805271455449088
   
'''

# @pintia code=start
double_numbers = []
def main():
    s = input().split()
    single_numbers = s[1:]
    
    get_double_numbers(single_numbers)

    print_sum()
    
    
def get_double_numbers(single_numbers):
    for i in single_numbers:
        for j in single_numbers:
            if i == j:
                continue
            combine = i + j
            if combine not in double_numbers:
                double_numbers.append(combine)


def print_sum():
    sum = 0
    for i in double_numbers:
        sum += int(i)
        
    print(sum)

main()

# @pintia code=end