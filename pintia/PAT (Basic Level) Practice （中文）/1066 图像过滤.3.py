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

    rows = []
    # get rows
    for i in range(m):
        row =input().split()
        rows.append(row)
        
    # change rows
    for row in rows:
        for i in range(len(row)):
            row[i] = int(row[i])
            if row[i] >= a and row[i] <= b:
                row[i] = target
      
    # print rows
    for row in rows:
        for i in range(len(row)):
            if i != 0:
                print(" ", end="")
            print(f"{row[i]:03}", end="")
        print()

main()

# @pintia code=end