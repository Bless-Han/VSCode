'''
   @pintia psid=15 pid=826 compiler=PYTHON3
   
   ProblemSet: 数据结构与算法题目集（中文）
   
   Title: 7-19 求链式线性表的倒数第K项
   
   https://pintia.cn/problem-sets/15/exam/problems/826
   
'''
# @pintia code=start
def main():
    k = int(input())
    nums = []
    while True:
        n = int(input())
        if n < 0:
            break
        nums.append(n)
    if k > len(nums):
        print("NULL")
    else:
        print(nums[-k])
        



# @pintia code=end