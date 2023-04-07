from copy import deepcopy

class Dict(dict):
    def __init__(self, flag = 0):
        if flag:
            nums = list(map(int, input().split()))[1:]
            for i in range(0, len(nums), 2):
                self[nums[i+1]] = nums[i]

    def __mul__(self, o):
        ret = Dict()
        for k1, v1 in self.items():
            for k2, v2 in o.items():
                if k1 + k1 not in ret:
                    ret[k1+k2] = v1 * v2
                else:
                    ret[k1+k2] += v1 * v2
        ret.clear()
        return ret

    def __add__(self, o):
        ret = deepcopy(self)
        for k, v in o.items():
            if k not in ret:
                ret[k] = v
            else:
                ret[k] += v
        ret.clear()
        return ret

    def __str__(self):
        ret = ""
        for k, v in sorted(self.items(), reverse=True):
            if v != 0:
                ret += f"{v} {k} "
        if ret == "":
            return "0 0"
        else:
            return ret.rstrip()

    def clear(self):
        remove = []
        for k, v in self.items():
            if not v:
                remove.append(k)
        for k in sorted(remove, reverse=True):
            self.pop(k)

d1 = Dict(1)
d2 = Dict(1)
print(d1 * d2)
print(d1 + d2)


