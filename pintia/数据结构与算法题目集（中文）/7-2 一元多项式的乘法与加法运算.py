'''
   @pintia psid=15 pid=710 compiler=PYTHON3
   
   ProblemSet: 数据结构与算法题目集（中文）
   
   Title: 7-2 一元多项式的乘法与加法运算
   
   https://pintia.cn/problem-sets/15/exam/problems/710
   
'''
# @pintia code=start
import numpy as np

f_coeffs = [3, 2, -5, 7]
g_coeffs = [4, 0, -1]
f = np.poly1d(f_coeffs)
g = np.poly1d(g_coeffs)
h = f + g

# @pintia code=end