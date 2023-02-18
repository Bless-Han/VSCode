'''
   @pintia psid=994805260223102976 pid=994805279328157696 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1044 火星数字
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805279328157696
   
'''
# @pintia code=start
def change(s):
    heigh_index = ["tam", "hel", "maa", "huh", "tou", "kes",
             "hei", "elo", "syy", "lok", "mer", "jou"]
    low_index = ["tret", "jan", "feb", "mar", "apr", "may", "jun", "jly",
           "aug", "sep", "oct", "nov", "dec"]
    try:
        number = int(s)
        heigh_number = number // 13
        low_number = number % 13
    except ValueError:
        ...


n = int(input())
for _ in range(n):
    print(change(input))

# @pintia code=end