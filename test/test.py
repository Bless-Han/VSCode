import decimal
a = input()
e_l, exp = a.split("E")
p_l, p_r = e_l.split(".")
n = -(len(p_r)) + int(exp)
n = -n if n < 0 else 0
print(f"{decimal.Decimal(a):.{n}f}")
