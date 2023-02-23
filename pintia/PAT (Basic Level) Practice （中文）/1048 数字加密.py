'''
   @pintia psid=994805260223102976 pid=994805276438282240 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1048 数字加密
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805276438282240
   
'''
# @pintia code=start
def change(a, b):
    a = a[::-1]
    b = b[::-1]

    ret_list = []
    b_more_a = len(b) - len(a)
    if b_more_a > 0:
        a += '0' * b_more_a
        max_len = len(b)
    elif b_more_a < 0:
        b += '0' * -b_more_a
        max_len = len(a)
    else:
        max_len = len(b)
    ret_list = list(b)
    
    quyu_str = "0123456789JQK"
    for i in range(max_len):
        if (i + 1) % 2 == 1:
            # 取余13
            ret_list[i] = quyu_str[(int(a[i]) + int(b[i])) % 13]
        else:
            # b - a
            temp_number = int(b[i]) - int(a[i])
            ret_list[i] = str(temp_number + 10) if temp_number < 0 else str(temp_number)
    
    return reversed(ret_list)
    
a, b = input().split()

print(*change(a, b), sep='')

# @pintia code=end
""" @pintia test=start
967 321


@pintia test=end """