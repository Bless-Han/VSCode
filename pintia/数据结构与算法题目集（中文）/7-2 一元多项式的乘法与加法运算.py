'''
   @pintia psid=15 pid=710 compiler=PYTHON3
   
   ProblemSet: 数据结构与算法题目集（中文）
   
   Title: 7-2 一元多项式的乘法与加法运算
   
   https://pintia.cn/problem-sets/15/exam/problems/710
   
'''
# @pintia code=start
from copy import deepcopy

class Dict(dict):
    def __str__(self):
        if not self:
            return "0 0"
        else:
            return " ".join(f"{xishu} {zhishu}" for zhishu, xishu in sorted(self.items(), reverse=True))

    def __add__(self, other):
        ret = deepcopy(self)
        for zhishu, xishu in other.items():
            if zhishu in ret:
                ret[zhishu] += xishu
            else:
                ret[zhishu] = xishu
        return Dict({key: value for key, value in ret.items() if value})

    def __mul__(self, other):
        ret = {}
        for zhishu1, xishu1 in self.items():
            for zhishu2, xishu2 in other.items():
                add_zhishu = zhishu1 + zhishu2
                mul_xishu = xishu1 * xishu2
                if add_zhishu in ret:
                    ret[add_zhishu] += mul_xishu
                else:
                    ret[add_zhishu] = mul_xishu
        return Dict({key: value for key, value in ret.items() if value})


lst1 = list(map(int, input().split()))[1:]
dic1 = Dict({lst1[i+1]: lst1[i] for i in range(0, len(lst1), 2)})
lst2 = list(map(int, input().split()))[1:]
dic2 = Dict({lst2[i+1]: lst2[i] for i in range(0, len(lst2), 2)})
print(dic1 * dic2)
print(dic1 + dic2)



# @pintia code=end
""" @pintia test=start
4 3 4 -5 2  6 1  -2 0
0 -3 4 5 2 -6 1 2 0

@pintia test=end """