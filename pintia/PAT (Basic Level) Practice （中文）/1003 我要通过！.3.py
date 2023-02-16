'''
   @pintia psid=994805260223102976 pid=994805323154440192 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1003 我要通过！
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805323154440192
   
'''

# @pintia code=start
def full_A(s):
    for c in s:
        if c != "A":
            return False

    return True


def judge(s):
    p_index = s.find("P")
    t_index = s.rfind("T")
    p_count = s.count("P")
    t_count = s.count("T")
    if p_count != 1 or t_count != 1:
        return False
    left = s[:p_index]
    middle = s[p_index + 1: t_index]
    right = s[t_index + 1:]
    if full_A(left) == False or full_A(middle) == False or full_A(right) == False:
        return False

    return len(left) * len(middle) == len(right) and len(middle) > 0


n = int(input())
for i in range(n):
    s = input().strip()
    print("YES") if judge(s) else print("NO")


# @pintia code=end