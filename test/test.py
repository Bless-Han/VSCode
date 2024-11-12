m = 0
w = (1100 - 100 * m) / 300
while w != int(w):
    m += 1
    w = (1100 - 100 * m) / 300
print(m, w)
