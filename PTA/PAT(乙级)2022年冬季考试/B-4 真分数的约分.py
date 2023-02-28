a, b = input().split()
same = []
c, d = a, b
for char in c:
	if char in d:
		c = c.replace(char, "", 1)
		d = d.replace(char, "", 1)

a, b, c, d = int(a), int(b), int(c), int(d)

print(f"{a}/{b} == {c}/{d}") if a/b == c/d else print(f"{a}/{b} != {c}/{d}")