'''
   @pintia psid=994805260223102976 pid=994805262622244864 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1076 Wifi密码
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805262622244864
   
'''

# @pintia code=start
change = {"A": "1", "B": "2", "C": "3", "D": "4"}
def main():
    n = int(input())
    s = []
    # TODO 获取接下来所有的数据
    for i in range(n):
        s.extend(input().split())

    print(get_number(s))



def get_number(s):
    ret = ""
    for v in s:
        if v[-1] == "T":
            ret += change[v[0]]
            
    return ret 


main()
# @pintia code=end