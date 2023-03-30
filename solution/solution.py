import copy
class Multi:
    def __init__(self, lst: list[int] = []):
        self.dic = {}
        for i in range(0, len(lst), 2):
            self.dic[lst[i+1]] = lst[i]


    def __str__(self):
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
        ret.dic = dic
        return ret


mu1 = list(map(int, input().split()))[1:]
mu2 = list(map(int, input().split()))[1:]
multi1 = Multi(mu1)
multi2 = Multi(mu2)
print("multi1", multi1)
print("multi2", multi2)

print(multi1 + multi2)

print("Ok")
