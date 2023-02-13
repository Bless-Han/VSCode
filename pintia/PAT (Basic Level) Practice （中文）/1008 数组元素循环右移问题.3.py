'''
   @pintia psid=994805260223102976 pid=994805316250615808 compiler=PYTHON3
   
   ProblemSet: PAT (Basic Level) Practice （中文）
   
   Title: 1008 数组元素循环右移问题
   
   https://pintia.cn/problem-sets/994805260223102976/problems/994805316250615808
   
'''

# @pintia code=start
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
m = m % n
print(numbers[-m:] + numbers[:-m])




# @pintia code=end