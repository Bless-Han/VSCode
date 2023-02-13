'''
   @pintia psid=994805260223102976 pid=994805323154440192 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1003 我要通过！
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805323154440192
   
'''

# @pintia code=start
def main():
    n = int(input())
    for i in range(n):
        s = input().strip()
        print("YES") if is_pat(s) else print("NO")

    
def is_pat(s):
    # indexes = [x1, x2], x1 和 x2 分别为始坐标和未坐标
    # "pat" == s[x1:x2]
    indexes = get_pat(s)
    if indexes[0] == -1 or indexes[1] == -1:
        return False

    left = s[:indexes[0]]
    right = s[indexes[1] + 1:]
    # 判断是否由A组成
    if judge_a(left + right) == False:
        return False
    middle_len = len(s[indexes[0]: indexes[1] + 1]) - 2
    return (left * middle_len) == right
    

def get_pat(s):
    ret = [-1, -1]
    index = 0
    # find "P"
    l = len(s)
    for i in range(l):
        if s[i] == "P":
            ret[0] = i
            break
    found_a = False
    if ret[0] != -1:
        for i in range(ret[0] + 1, l):
            if s[i] == "A":
                found_a = True
                continue
            elif found_a == True and s[i] == "T":
                ret[1] = i
                break
            elif found_a == False:
                break
    return ret


def judge_a(s):
    for c in s:
        if c != "A":
            return False
    return True

main()
# @pintia code=end