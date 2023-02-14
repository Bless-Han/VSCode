'''
   @pintia psid=994805260223102976 pid=994805308755394560 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1014 福尔摩斯的约会
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805308755394560
   
'''

# @pintia code=start
def get_week_hour(s1, s2):
    weeks = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    week = "N"
    hour = 0
    l = min(len(s1), len(s2))
    for i in range(l):
        if s1[i] == s2[i]:
            if week == "N" and "A" <= s1[i] <= "G":
                week = weeks[ord(s1[i]) - ord("A")]
                continue
            if week != "N":
                if "0" <= s1[i] <= "9":
                    hour = int(s1[i])
                    break
                elif "A" <= s1[i] <= "O":
                    hour = 10 + (ord(s1[i]) - ord("A"))
                    break

    return [week, hour]

def get_minute(s3, s4):
    minute = 0
    l = min(len(s3), len(s4))
    for minute in range(l):
        if s3[minute] == s4[minute] and s3[minute].isalpha():
            break
        minute += 1
    return minute


s1 = input()
s2 = input()
s3 = input()
s4 = input()
week, hour = get_week_hour(s1, s2)
minute = get_minute(s3, s4)

print(f"{week} {hour:02}:{minute:02}")




# @pintia code=end