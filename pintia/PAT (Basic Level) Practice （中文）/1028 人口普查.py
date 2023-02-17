'''
   @pintia psid=994805260223102976 pid=994805293282607104 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1028 人口普查
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805293282607104
   
'''
# @pintia code=start
n = int(input())
old = {"name": "", "birthday": 0}
young = {"name": "", "birthday": 0}
count = 0
for i in range(n):
    name, birthday_str = input().split()
    birthday_int = int("".join(birthday_str.split("/")))
    if 18140906 <= birthday_int <= 20140906:
        count += 1
        if old["name"] == "":
            old["name"] = name
            old["birthday"] = birthday_int
            young["name"] = name
            young["birthday"] = birthday_int
        else:
            if old["birthday"] > birthday_int:
                old["name"] = name
                old["birthday"] = birthday_int
            if young["birthday"] < birthday_int:
                young["name"] = name
                young["birthday"] = birthday_int

print(count, old["name"], young["name"])


# @pintia code=end
""" @pintia test=start
2
John 2001/05/12
James 1814/09/05
@pintia test=end """