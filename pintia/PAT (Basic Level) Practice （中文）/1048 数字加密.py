'''
   @pintia psid=994805260223102976 pid=994805276438282240 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1048 数字加密
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805276438282240
   
'''
# @pintia code=start
def change(a, b):
    left = ""
    if len(b) > len(a):
        left += b[len(a): ]
    a_l = len(a)
    print(left)
    
    quyu_str = "0123456789JQK"
    right = ""
    for i in range(a_l):
        if (i + 1) % 2 == 0:
            # 取余13后的数字
            right += quyu_str[(int(a[i]) + int(b[i])) % 13]
        else:
            # b - a
            temp_number = int(b[i]) - int(a[i])
            right += str(temp_number + 10) if temp_number < 0 else right + str(temp_number)
    
    return (left + right)[::-1]
    
a, b = input().split()
a = a[::-1]
b = b[::-1]

print(change(a, b))

# @pintia code=end