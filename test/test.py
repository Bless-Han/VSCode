from copy import deepcopy
class Dict(dict):
    def __init__(self, flag=0):
        if flag == 1:
            numbers = list(map(int, input().split()))[1:]
            for i in range(0, len(numbers), 2):
                dict[i+1] = i

    def __str__(self):
        ret = []
        self.clear()
        if not self:
            return "0 0"
        for k, v in sorted(self.items(), reverse=True):
            ret.append()
        return " ".join(str(n) for n in ret)

a = []
a.append("a")
a.append("b")
