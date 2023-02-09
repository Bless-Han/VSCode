'''
   @pintia psid=994805260223102976 pid=994805264312549376 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1071 小赌怡情
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805264312549376
   
'''

# @pintia code=start
x = 0
def main():
    global x
    s = input().split()
    x, k = map(int, s)
    
    for i in range(k):
        if x <= 0:
            print("Game Over.")
            break
        s = input().split()
        n1, b, t, n2 = map(int, s)
        if x < t:
            print(f"Not enough tokens.  Total = {x}.")
            continue

        # judge = 0 if n2 < n1, else judge = 1
        judge = 0 if n2 < n1 else 1
        
        if judge == b:
            x += t
            print(f"Win {t}!  Total = {x}.")
        else:
            x -= t 
            print(f"Lose {t}.  Total = {x}.")



main()
# @pintia code=end