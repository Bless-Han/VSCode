'''
   @pintia psid=994805260223102976 pid=994805323154440192 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1003 我要通过！
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805323154440192
   
'''
# @pintia code=start
def a_judge(a):
    for c in a:
        if c != "A":
            return False
    return True


def s_judge(s):
    s = s.strip()
    try:
        p_index = s.index("P")
        t_index = s.index("T")
    except ValueError:
        return False
    
    a_left = s[:p_index]
    a_middle = s[p_index + 1: t_index]
    a_right = s[t_index + 1: ]

    if len(a_middle) == 0:
        return False
    
    if a_judge(a_left) == False or a_judge(a_middle) == False or a_judge(a_right) == False:
        return False
    
    return len(a_left) * len(a_middle) == len(a_right)

n = int(input())

for _ in range(n):
    s = input()
    print("YES") if s_judge(s) else print("NO")



# @pintia code=end