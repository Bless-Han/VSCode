'''
   @pintia psid=994805260223102976 pid=994805297229447168 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1024 科学计数法
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805297229447168
   
'''
# @pintia code=start
left, right = input().split("E")
zhengshu, xiaoshu = left.split(".")

result = "" if zhengshu[0] == "+" else "-"
zhengshu = zhengshu[1:]
hebing = zhengshu + xiaoshu

right_sign = "-" if right[0] == "-" else "+"
right_int = int(right[1:])
if right_sign == "-":
    result += "0." + "0" * (right_int - 1) + hebing
else:
    if right_int >= len(xiaoshu):
        result += hebing + "0" * (right_int - len(xiaoshu))
    else:
        point_location = right_int + 1
        result += hebing[ :point_location] + "." + hebing[point_location: ]


print(result)

# @pintia code=end
""" @pintia test=start
+1.23400E+04
@pintia test=end """