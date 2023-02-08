'''
   @pintia psid=994805260223102976 pid=994805285812551680 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1036 跟奥巴马一起编程
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805285812551680
   
'''

# @pintia code=start
# init
"""
dkslfsldkjfls jsfj lsdf 
sdlfsd jklf
"""
s = input().split()
n = int(s[0])
c = s[1]

space = " "
# print the top line
print(c *  n)

# print the middle of the figure
for row in range(0, int(round((n + 0.000001) / 2) - 2)):
   print(f"{c}{space * (n - 2)}{c}")

# print the bottom line
print(c *  n)


# @pintia code=end
""" @pintia test=start
11 a
@pintia test=end """
""" @pintia test=start
1 a
@pintia test=end """
""" @pintia test=start
2 a
@pintia test=end """