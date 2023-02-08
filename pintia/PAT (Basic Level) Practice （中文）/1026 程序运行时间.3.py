'''
   @pintia psid=994805260223102976 pid=994805295203598336 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1026 程序运行时间
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805295203598336
   
'''

# @pintia code=start
# change seconds to time(xx:xx:xx)
def change(seconds):
    minutes = 0
    hours = 0
    local_seconds = round(seconds % 60 + 0.0001)
    seconds //= 60
    if seconds > 0:
        minutes = round(seconds % 60 + 0.0001)
        seconds //= 60
    if seconds > 0:
        hours = round(seconds % 60 + 0.0001)
    return f"{hours:02}:{minutes:02}:{local_seconds:02}"
    
   



s = input().split()
c1, c2 = map(int, s)
print(change((c2 - c1) / 100))


# @pintia code=end
