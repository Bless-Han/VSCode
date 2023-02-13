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
        print("YES") if is_pat() else print("NO")

    
def is_pat():
    s = input().strip()
    index = s.find("PAT")
    # number is use to add to index
    number = 3
    if index == -1:
        index = s.find("PAAT")
        number = 4
    if index == -1:
        return False
    before = s[:index] 
    after = s[index+number: ]
    if before == after:
        s = before + after
        new_s = s.replace(" ", "").replace("A", "")
        return len(new_s) == 0
    else:
        return False



main()
# @pintia code=end