'''
   @pintia psid=994805260223102976 pid=994805277847568384 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1046 划拳
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805277847568384
   
'''

# @pintia code=start
han_huas = []
def main():
    n = input()

    for i in range(int(n)):
        jia_han, jia_hua, yi_han, yi_hua = input().split()
        han_huas.append({"jia_han": jia_han, "jia_hua": jia_hua,
                     "yi_han": yi_han, "yi_hua": yi_hua})
    
    get_result()
    

def get_result():
    jia_he = 0
    yi_he = 0

    for han_hua in han_huas:
        qiuhe = str(int(han_hua["jia_han"]) + int(han_hua["yi_han"]))
        if han_hua["jia_hua"] == qiuhe and han_hua["yi_hua"] != qiuhe:
            yi_he += 1
        elif han_hua["jia_hua"] != qiuhe and han_hua["yi_hua"] == qiuhe:
            jia_he += 1

    print(jia_he, yi_he)


   


main()

# @pintia code=end