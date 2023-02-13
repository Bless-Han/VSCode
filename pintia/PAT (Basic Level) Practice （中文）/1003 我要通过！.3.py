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
    # indexes = [x1, x2], x1 和 x2 分别为始坐标和未坐标+1
    # "pat" == s[x1:x2]
    indexes = get_pat(s)
    left = 
    if indexes[0] == -1 or indexes[1] == -1:
        return False
    

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
            elif found_a == True and s[i] == "P":
                ret[1] = i + 1
                break
            elif:
                


    return ret



main()
# @pintia code=end