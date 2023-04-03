'''
求链式线性表的倒数第K项:

给定一系列正整数，请设计一个尽可能高效的算法，查找倒数第K个位置上的数字。

输入格式:
输入首先给出一个正整数K，随后是若干非负整数，最后以一个负整数表示结尾（该负数不算在序列内，不要处理）。

输出格式:
输出倒数第K个位置上的数据。如果这个位置不存在，输出错误信息NULL。

输入样例:
4 1 2 3 4 5 6 7 8 9 0 -1 (the nums in the same line)
输出样例:
7
'''

def main():
    # Q: the nums is too big, and all nums in the same line, how to input?
    # Q: How can I read nums from the s?
    
    s = input()
    # Q: I can't use the split(), because the nums is too big, and all nums in the same line.
    k = int(s.split()[0])
    
    nums = []
    while True:
        n = int(input())
        if n < 0:
            break
        nums.append(n)