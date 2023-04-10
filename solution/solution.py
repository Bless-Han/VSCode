s = input()
left, right = s.split("E")
count = len(left) - 1 + int(right)
print(f"{float(s):.{count}f}")
