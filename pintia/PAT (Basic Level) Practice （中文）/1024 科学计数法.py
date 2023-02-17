'''
   @pintia psid=994805260223102976 pid=994805297229447168 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1024 科学计数法
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805297229447168
   
'''
# @pintia code=start
left, right = input().split("E")
result = ""
if left[0] == "-":
    result += "-"
left = left[1:]

# E 右边的那个数字
right_number = int(right[0] + str(int(right[1:])))

if right_number == 0:
    result += left
elif right_number < 0:
    left = left.replace(".", "")
    result += "0." + "0" * (abs(right_number) - 1) + left
else:
    left = left.replace(".", "")
    # right_of_point：小数点右边的长度
    right_of_point = len(left) - 1
    if right_number >= right_of_point:
        result += left + "0" * (right_number - right_of_point)
    else:
        # point_location 小数点新的位置
        point_location = right_number + 1
        left = list(left)
        left.insert(point_location, ".")
        result += "".join(left)
        

print(result)

# @pintia code=end
""" @pintia test=start
+1.23400E+05
@pintia test=end """