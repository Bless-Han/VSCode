import copy
class Multi:
    def __init__(self, lst: list[int] = []):
        self.dic = {}
        for i in range(0, len(lst), 2):
            self.dic[lst[i+1]] = lst[i]


    def __str__(self):
        if not self.dic:
            return "0 0"
        ret = ""
        for k in sorted(self.dic, reverse=True):
            ret += f"{self.dic[k]} {k} "
        return ret.strip()


    def __add__(self, other):
        ret = Multi()
        dic = copy.deepcopy(self.dic)
        for k in other.dic:
            if k in dic:
                dic[k] += other.dic[k]
            else:
                dic[k] = other.dic[k]
        ret.dic = {k: v for k, v in dic.items() if v}
        return ret


    def __mul__(self, other):
        ret = Multi()
        dic = {}
        for zhishu1, xishu1 in self.dic.items():
            for zhishu2, xishu2 in other.dic.items():
                add_zhishu = zhishu1 + zhishu2
                mul_xishu = xishu1 * xishu2
                if add_zhishu in dic:
                    dic[add_zhishu] += mul_xishu
                else:
                    dic[add_zhishu] = mul_xishu
        ret.dic = {k: v for k, v in dic.items() if v}
        return ret


mu1 = list(map(int, input().split()))[1:]
mu2 = list(map(int, input().split()))[1:]
multi1 = Multi(mu1)
multi2 = Multi(mu2)

print(multi1 * multi2)
print(multi1 + multi2)

