


class Dict(dict):
    def __mul__(self, o):
        ret = Dict()
        for k1, v1 in self.items():
            for k2, v2 in o.items():
                if v1 + v1 not in ret:
                    ret[v1+v2] = k1 * k2
                else:
                    ret[v1+v2] += k1 * k2
        return ret

    def __add__(self, o):
        ret = deepcopy(self)
        for k, v in o.items():
            if v not in ret:
                ret[k] = v
            else:
                ret[k] += v
        return ret

    def __str__(self):
        return "good"

d1 = Dict()
d2 = Dict()
print(d1 * d2)
print(d1 + d2)

print("OK")
