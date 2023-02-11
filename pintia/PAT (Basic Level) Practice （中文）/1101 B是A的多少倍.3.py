'''
   @pintia psid=994805260223102976 pid=1478634052026146816 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1101 B是A的多少倍
   
   https://pintia.cn/problem-sets/994805260223102976/problems/1478634052026146816
   
'''

# @pintia code=start
def main():
    s = input().split()
    a, d = map(int, s)
    str_a = str(a)
    b = int(str_a[-d:] + str_a[:len(str_a) - d])
    print(f"{b / a:.2f}")


main()
# @pintia code=end