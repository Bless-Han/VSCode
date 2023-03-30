class Dict(dict):
    def __str__(self):
        return " ".join(f"{xishu} {zhishu}" for zhishu, xishu in self.items())



a = {"height": 0, "length": 90}
b = Dict(a)

print(b)
