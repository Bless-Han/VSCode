n = int(input())
bu = "23574"
yuan = "018"
dao = {"6":"9", "9":"6"}
res = []
for i in range(n):
    flag = True
    tmps = ""
    s = input()
    for c in s:
        if c in bu:
            flag = False
            break
        elif c in yuan:
            tmps += c
        elif c in dao:
            tmps += dao[c]
    if flag == False:
        res.append("bu ke neng")
    else:
        res.append(tmps)
for s in res:
    print(s)