'''
   @pintia psid=994805260223102976 pid=994805268817231872 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1061 判断题
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805268817231872
   
'''

# @pintia code=start
def main():
    n, m = input().split()
    fenzhi = input().split()
    right_answer = input().split()

    for i in range(int(n)):
        answer = input().split()
        print_score(answer, fenzhi, right_answer)
        


def print_score(answer, fenzhi, right_answer):
    result = 0
    
    for i in range(len(right_answer)):
        if answer[i] == right_answer[i]:
            result += int(fenzhi[i])
    
    print(result)


   


main()

# @pintia code=end