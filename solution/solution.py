n = int(input())

modified = "1lO0"
to_char = "@Lo%"
for _ in range(n):
    name, password = input().split()
    password_list = list(password)
    change = False
    replace = []

    for i in range(len(password_list)):
        print(password_list[i], change)
        if password_list[i] in modified:
            password_list[i] = to_char[modified.index(password_list[i])]
            change = True
    if change:
        replace.append(f"{name} {''.join(password_list)}")

if replace:
    for row in replace:
        print(row)
else:
    print(f"There is {n} account and no account is modified")

