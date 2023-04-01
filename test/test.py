a = input()
e_l, exp = a.split("E")
p_l, p_r = e_l.split(".")
n = -(len(p_r)) + int(exp)
if n > 0:
    n = 0
else:
    n = -n
print(f"{float(a):.{n}f}")
