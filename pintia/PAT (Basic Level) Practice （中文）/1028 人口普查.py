'''
   @pintia psid=994805260223102976 pid=994805293282607104 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1028 人口普查
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805293282607104
   
'''
# @pintia code=start
n = int(input())
old = {"name": "", "birthday": ""}
young = {"name": "", "birthday": ""}
count = 0
for i in range(n):
    name, birthday_str = input().split()
    if "1814/09/06" <= birthday_str <= "2014/09/06":
        count += 1
        if old["name"] == "":
            old["name"] = name
            old["birthday"] = birthday_str
            young["name"] = name
            young["birthday"] = birthday_str
        else:
            if old["birthday"] > birthday_str:
                old["name"] = name
                old["birthday"] = birthday_str
            if young["birthday"] < birthday_str:
                young["name"] = name
                young["birthday"] = birthday_str

if count > 0:
    print(count, old["name"], young["name"])
elif count == 0:
    print("0")


# @pintia code=end
""" @pintia test=start
2
John 2001/05/12
James 1814/09/05
@pintia test=end """