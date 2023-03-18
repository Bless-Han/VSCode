
result = 1
wtl = {}
for _ in range(3):
    w, t, l = map(float, input().split())
    wtl["W"] = w
    wtl["T"] = t
    wtl["L"] = l
    # max
    mx = max(wtl.items(), key=lambda x: x[1])
    print(mx[0] + " ", end="")
    result *= mx[1]
print(f"{(result * 0.65 - 1) * 2:.2f}")
