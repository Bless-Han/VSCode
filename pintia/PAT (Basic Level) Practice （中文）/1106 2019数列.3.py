'''
   @pintia psid=994805260223102976 pid=1478634404943273984 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1106 2019数列
   
   https://pintia.cn/problem-sets/994805260223102976/problems/1478634404943273984
   
'''

# @pintia code=start
def main():
    x = "2019"
    n = int(input())

    if n <= 4:
        print(x[:n])
    else:
        for i in range(4, n):
            x += count(x[-4:])

        print(x)

    

def count(s):
    a, b, c, d = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    sum = a + b + c + d
    return str(sum % 10)


main()
# @pintia code=end