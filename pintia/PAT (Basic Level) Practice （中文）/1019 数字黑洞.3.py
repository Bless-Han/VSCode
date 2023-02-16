'''
   @pintia psid=994805260223102976 pid=994805302786899968 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1019 数字黑洞
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805302786899968
   
'''

# @pintia code=start
def change(n):
    if n < 10: return n * 1000
    elif n < 100: return n * 100
    elif n < 1000: return n * 10
    else: return n
    
    
n = input()

while True:
    a = int("".join(sorted(n, reverse=True)))
    a = change(a)
    b = int("".join(sorted(n)))
    n = str(a - b)
    print(f"{a:04} - {b:04} = {a - b:04}")
    if n == "6174" or n == "0":
        break



# @pintia code=end