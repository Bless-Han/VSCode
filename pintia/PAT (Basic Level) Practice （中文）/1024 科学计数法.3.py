'''
   @pintia psid=994805260223102976 pid=994805297229447168 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1024 科学计数法
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805297229447168
   
'''

# @pintia code=start
left, right = input().split("E")
left = left.replace(".", "")

result = ""
if left[0] == "-":
    left = left[1:]
    result += "-"
elif left[0] == "+":
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

print(result)

# @pintia code=end
""" @pintia test=start
-1.2345E-2
@pintia test=end """
""" @pintia test=start
-1.2345E-6
@pintia test=end """