n = int(input())
count = 0

s = ""
while True:
	s = input()
	count += s.count("(zhangsheng)")
	if s[-1] == "#":
		break

print(str(count) + " True") if count == n else print(str(count) + " False")
