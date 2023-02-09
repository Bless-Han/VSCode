'''
   @pintia psid=994805260223102976 pid=994805266514558976 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1066 图像过滤
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805266514558976
   
'''

# @pintia code=start
def main():
    s = input().split()
    m, n, a, b, target = map(int, s)

    for i in range(m):
        row = input().split()
        row = list(map(int, row))
        for i, v in enumerate(row):
            if i != 0:
                print(" ", end="")
            if v >= a and v <= b:
                v = target 
            print(f"{v:03}", end="")
        print()
            

main()

# @pintia code=end