class Dict(dict):
    def __init__(self):
        s = list(map(int, input().split()))[1:]
        for i in range(0, len(s), 2):
            if s[i] in self:
                self[s[i+1]] += s[i]
            else:
                self[s[i+1]] = s[i]

    def __str__(self):
        return "Hello world"

    def __add__(self, other):
        ...

    def __mul__(self, other):
        ...

a = Dict()
b = Dict()
print(a + b)
print(a * b)

