'''
   @pintia psid=994805260223102976 pid=994805279328157696 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1044 火星数字
   
   https://pintia.cn/problem-sets/994805260223102976/exam/problems/994805279328157696
   
'''
# @pintia code=start
def change(s):
    height_index = ["", "tam", "hel", "maa", "huh", "tou", "kes",
             "hei", "elo", "syy", "lok", "mer", "jou"]
    low_index = ["tret", "jan", "feb", "mar", "apr", "may", "jun", "jly",
           "aug", "sep", "oct", "nov", "dec"]
    try:
        number = int(s)
        height_str = height_index[number // 13]
        low_str = low_index[number % 13]
        # 调整高位字符
        if height_str != "":
            height_str += " "
        # 调整低位字符
        if low_str == "tret" and height_str != "":
            height_str = height_str.strip()
            low_str = ""

        return height_str + low_str
    except ValueError:
        s = s.split()
        height_number, low_number = 0, 0
        if len(s) == 1:
            try:
                height_number = height_index.index(s[0])
            except ValueError:
                low_number = low_index.index(s[0])
        else:
            height_str, low_str = s
            height_number = height_index.index(height_str)
            low_number = low_index.index(low_str)

        return height_number * 13 + low_number


n = int(input())
for _ in range(n):
    print(change(input()))

# @pintia code=end
""" @pintia test=start
1
13
@pintia test=end """