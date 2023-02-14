'''
   @pintia psid=994805260223102976 pid=994805311146147840 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1012 数字分类
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805311146147840
   
'''

# @pintia code=start
a1 = "N"
a2 = "N"
a3 = "N"
a4 = "N"
a5 = "N"

s = input().split()
numbers = list(map(int, s[1:]))

# for number % == 1
jiaocuo = 1

for number in numbers:
    match number % 5:
        case 0:
            if number % 2 == 0:
                if a1 == "N":
                    a1 = number
                else:  
                    a1 += number
        case 1:
            if a2 == "N":
                a2 = number
            else:
                a2 += number * jiaocuo
            jiaocuo *= -1
        case 2:
            if a3 == "N":
                a3 = 1
            else:
                a3 += 1
        case 3:
            if a4 == "N":
                count = 1
                sum = number
                a4 = ""
            else:
                count += 1
                sum += number
        case 4:
            if a5 == "N":
                a5 = number
            elif number > a5:
                a5 = number

if a4 != "N":
    a4 = round(sum / count + 0.001, 1)



print(a1, a2, a3, a4, a5)

# @pintia code=end