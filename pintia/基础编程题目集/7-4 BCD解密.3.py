'''
   @pintia psid=14 pid=784 compiler=PYTHON3
   
   ProblemSet: 基础编程题目集
   
   Title: 7-4 BCD解密
   
   https://pintia.cn/problem-sets/14/problems/784
   
'''

# @pintia code=start
s = input().split()
n = int(s[0])
c = s[1]

space = " "
print(c *  n)
for row in range(1, round(n / 2) - 2):
   print(f"{c}{space * (n - 2)}{c}")

print(c *  n)


# @pintia code=end
""" @pintia test=start
Put your custom test sample here
@pintia test=end """