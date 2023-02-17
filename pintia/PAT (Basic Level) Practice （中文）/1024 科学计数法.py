'''
   @pintia psid=994805260223102976 pid=994805297229447168 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1024 科学计数法
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805297229447168
   
'''
# @pintia code=start
left, right = input().split("E")
left = left.replace(".", "")

result = ""
if left[0] == "-":
    result += "-"
left = left[1:]

if right[0] == "-":
    right_number = int(right.replace("-", ""))
    right_number -= 1
    result += "0." + "0" * right_number + left
elif right[0] == "+":
    right_number = int(right.replace("+", ""))
    if len(left) - 1 >= right_number:
        result += left[:right_number + 1] + "." + left[right_number + 1: ]
    else:
        result += left + "0" * (right_number - (len(left) - 1))

# 去前面的0
for i in range(len(result)):
    if result[i] != "0":
        break


print(result[i:])

# @pintia code=end