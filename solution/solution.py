a = input().split()
b = input().split()
c = []
for n in a:
    if n in b:
        c.append(n)
if len(c) == 0:
    print("NULL")
else:
    print(*c)
