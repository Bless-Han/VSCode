'''
   @pintia psid=994805260223102976 pid=1478634461852217344 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1107 老鼠爱大米
   
   https://pintia.cn/problem-sets/994805260223102976/problems/1478634461852217344
   
'''

# @pintia code=start
def main():
    s = input().split()
    n, m = map(int, s)
    wins = []
    for i in range(n):
        s = input().split()
        scores = map(int, s)
        win = max(scores)
        wins.append(win)
        if i != 0:
            print(" ", end="")
        print(win, end="")
    print()
    print(max(wins))


main()
# @pintia code=end