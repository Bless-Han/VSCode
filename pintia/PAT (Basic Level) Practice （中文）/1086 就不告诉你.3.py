'''
   @pintia psid=994805260223102976 pid=1038429065476579328 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1086 就不告诉你
   
   https://pintia.cn/problem-sets/994805260223102976/problems/1038429065476579328
   
'''

# @pintia code=start
# TODO 翻转str
def main():
    s = input().split()
    a, b = map(int, s)
    result_num = a * b
    result_str = str(result_num)
    print(result_str[::-1])

main()
# @pintia code=end