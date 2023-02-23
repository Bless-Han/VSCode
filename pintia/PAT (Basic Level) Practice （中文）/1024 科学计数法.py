'''
   @pintia psid=994805260223102976 pid=994805297229447168 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1024 科学计数法
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805297229447168
   
'''
# @pintia code=start
left, right = input().split("E")
left_sign = '' if left[0] == '+' else '-'
left = left[1: ]
point_left, point_right = left.split('.')
combine = point_left + point_right

right_number = int(right)

result = left_sign

if right_number >= 0:
    if right_number >= len(point_right):
        result += combine + "0" * (right_number - len(point_right))
    else:
        result += point_left + point_right[ : right_number] + '.' + point_right[right_number: ]
else:
    result += '0.' + '0' * (-right_number - 1) + combine
    
print(result)


# @pintia code=end
""" @pintia test=start
+1.23400E+04
@pintia test=end """