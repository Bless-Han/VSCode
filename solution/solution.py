
a = {'a': 1, 'b': '', 'c': 3, 'd': None}
b = {k: v for k, v in a.items() if v}
print(b)
