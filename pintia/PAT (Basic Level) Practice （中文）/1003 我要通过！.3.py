'''
   @pintia psid=994805260223102976 pid=994805323154440192 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1003 我要通过！
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805323154440192
   
'''

# @pintia code=start
def is_passed(s):
    if (s[0] == "A" or s[0] == "P") == False:
        return False
    # count the number of "A"
    # the index of 0 is left of "A", 2 is middle of "A", 4 is right of "A"
    count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    judge = "APATA"
    judge_index = 0
    for c in s:
        try:
            while judge[judge_index] != c:
                judge_index += 1
        except IndexError:
            return False
        count[judge_index] += 1
            
    #.有问题的代码:
    return count[0] * count[2] == count[4] and count[1] != 0 and count[2] != 0 and count[3] != 0
        
    # 正确的代码:
    # 需将代码从 != 0 改成 == 1 ------> count[1] == 1        count[3] == 1
    # return count[0] * count[2] == count[4] and count[1] == 1 and count[2] != 0 and count[3] == 1
        
    
    
# main
n = int(input().strip())

for i in (range(n)):
    print("YES") if is_passed(input()) else print("NO")


# @pintia code=end