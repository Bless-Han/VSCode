'''
堆中的路径
分数 25   提交人数 13668   通过人数 4854   通过率 35.51%
作者 陈越     单位 浙江大学
将一系列给定数字依次插入一个初始为空的小顶堆H[]。随后对任意给定的下标i，打印从H[i]到根结点的路径。

输入格式:
每组测试第1行包含2个正整数NN和MM(\le 1000≤1000)，分别是插入元素的个数、以及需要打印的路径条数。下一行给出区间[-10000, 10000]内的NN个要被插入一个初始为空的小顶堆的整数。最后一行给出MM个下标。

输出格式:
对输入中给出的每个下标i，在一行中输出从H[i]到根结点的路径上的数据。数字间以1个空格分隔，行末不得有多余空格。

输入样例:
5 3
46 23 26 24 10
5 4 3
输出样例:
24 23 10
46 23 10
26 10
'''

N, M = map(int, input().split())
H = [0]
nums = list(map(int, input().split()))
for num in nums:
    H.append(num)
    i = len(H) - 1
    while i > 1:
        if H[i] < H[i // 2]:
            H[i], H[i // 2] = H[i // 2], H[i]
            i = i // 2
        else:
            break
for i in map(int, input().split()):
    path = []
    while i > 0:
        path.append(H[i])
        i = i // 2
    print(*path)

# Path: test/temp.py