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
        print("YES") if judge(s) else print("NO")


def judge(s):
    pat_index = 0
    pat = "APATA"
    '''
        the index of 0 represent "A" of left, 1 represent "P", 2 represent "A" of middle
        3 represent "P", 4 represent "A" of right
    '''
    pat_count = [0, 0, 0, 0, 0]
    for c in s:
        try:
            while c != pat[pat_index]:
                pat_index += 1
            pat_count[pat_index] += 1
        except IndexError:
            return False
    
    return pat_count[1] == 1 and pat_count[3] == 1 and pat_count[0] * pat_count[2] == pat_count[4] and pat_count[2] != 0

main()
# @pintia code=end