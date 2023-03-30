class Dict(dict):
    def __str__(self):
        if not self:
            return "0 0"
        else:
            return " ".join(f"{xishu} {zhishu}" for zhishu, xishu in self.items())



a = {}
b = Dict({1:2, 2:3})

print(b)
