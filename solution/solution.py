class Dict(dict):
    def __add__(self, oth):
        ret = {k: v for k, v in self.items()}
        for k, v in oth.items():
            if k in ret:
                ret[k] += v
            else:
                ret[k] = v
        return Dict(ret)

    def __mul__(self, oth):
        ret = {}
        for k1, v1 in self.items():
            for k2, v2 in oth.items():
                if k1 + k2 in ret:
                    ret[k1 + k2] += v1 * v2
                else:
                    ret[k1 + k2] = v1 * v2
        return Dict(ret).clear()

    def __str__(self):
        self.clear()
        ret = ""
        for k, v in self.items():
            ret += f"{v} {k} "
        return ret.strip()

    def clear(self):
        self = {k: v for k, v in sorted(self.items(), key=lambda x: x[0], reverse=True) if v}

def toDict(lis):
    return Dict({lis[i+1]: lis[i] for i in range(0, len(lis), 2)})



a = list(map(int, input().split()))[1:]
b = list(map(int, input().split()))[1:]
a_dic = toDict(a)
b_dic = toDict(b)
print(a_dic * b_dic)
print(a_dic + b_dic)
