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

# 得到右边的数字
if right[0] == "-":
    right_number = int(right.replace("-", "")) * -1
elif right[0] == "+":
    right_number = int(right.replace("+", ""))

# 将结果组合到result
if right_number > 0:
    left = left.replace(".", "")
    # len(left) - 1 为小数点右边数字的长度
    if right_number >= len(left) - 1:
        result += left + "0" * (right_number - (len(left) - 1))
    else:
        # 计算小数点插入的位置
        point_location = right_number + 1
        l = list(left)
        l.insert(point_location, ".")
        result += "".join(l)
elif right_number < 0:
    left = left.replace(".", "")
    # 计算出前面插入0的个数
    right_number *= -1
    # right_number - 1: 减去"left"小数点左边那一位
    zero_count = right_number - 1
    result += "0." + "0" * zero_count + left
else:
    result += left

print(result)

# @pintia code=end
""" @pintia test=start
+1.23400E+04
@pintia test=end """