'''
   @pintia psid=994805260223102976 pid=994805275792359424 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1049 数列的片段和
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805275792359424
   
'''
# @pintia code=start
import sys
import decimal
aaaaaaa = input()
numbers = list(map(decimal.Decimal, sys.stdin.readline().split()))
result = decimal.Decimal(0)

# 临时计算
temp_a = decimal.Decimal(0)
# 求一个数的总计
sum_a_number = decimal.Decimal(0)
for i in range(len(numbers)):
    temp_a += numbers[i]
    sum_a_number += temp_a

for i in range(len(numbers)):
    if i == 0:
        result += sum_a_number
        continue
    else:
        # 求当前这个数的总计
        sum_a_number -= numbers[i - 1] * (len(numbers) - i + 1)

        result += sum_a_number

print(f"{result:.02f}")


# @pintia code=end
""" @pintia test=start
3
4 3 2 1
@pintia test=end """