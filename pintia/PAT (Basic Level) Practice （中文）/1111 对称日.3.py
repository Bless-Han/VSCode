'''
   @pintia psid=994805260223102976 pid=1621699285882593280 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1111 对称日
   
   https://pintia.cn/problem-sets/994805260223102976/problems/1621699285882593280
   
'''

# @pintia code=start
def main():
    months = {"Jan": "01", "Feb": "02", "Mar": "03",
    "Apr": "04", "May": "05", "Jun": "06",
    "Jul": "07", "Aug": "08", "Sep": "09",
    "Oct": "10", "Nov": "11", "Dec": "12"}
    n = int(input())
    
    for i in range(n):
        s = input().split()
        day = s[1].replace(",", "")
        day = f"{int(day):02}"
        month = months[s[0]]





main()
# @pintia code=end