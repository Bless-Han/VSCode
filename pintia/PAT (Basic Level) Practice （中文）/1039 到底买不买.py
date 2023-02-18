'''
   @pintia psid=994805260223102976 pid=994805283241443328 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1039 到底买不买
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805283241443328
   
'''
# @pintia code=start
# 判断数量是否够，返回多的数和缺的数
# -> (Bool, int, int)
def judge(buy_count, want_count):
    gouyong = True
    duo = 0
    que = 0
    for key in want_count:
        if key not in buy_count:
            gouyong = False
            que += want_count[key]
        elif want_count[key] - buy_count[key] > 0:
            gouyong = False
            que += want_count[key] - buy_count[key]
                
    if gouyong == True:
        global buy, want
        duo = len(buy) - len(want)

    return [gouyong, duo, que]


buy = input()
want = input()

buy_count = {}
want_count = {}
for c in buy:
    if c in buy_count:
        buy_count[c] += 1
    else:
        buy_count[c] = 1
        
for c in want:
    if c in want_count:
        want_count[c] += 1
    else:
        want_count[c] = 1
    
panduan = judge(buy_count, want_count)
print("Yes", panduan[1]) if panduan[0] else print("No", panduan[2])

# @pintia code=end
""" @pintia test=start
YrR8R
YrR8RrYY
@pintia test=end """