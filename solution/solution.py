N, M = map(int, input().split())
H = [0]
nums = list(map(int, input().split()))
for num in nums:
    H.append(num)
    i = len(H) - 1
    while i > 1:
        if H[i] < H[i // 2]:
            H[i], H[i // 2] = H[i // 2], H[i]
            i = i // 2
        else:
            break
print(H)
for i in map(int, input().split()):
    path = []
    while i > 0:
        path.append(H[i])
        i = i // 2
    print(*path)


