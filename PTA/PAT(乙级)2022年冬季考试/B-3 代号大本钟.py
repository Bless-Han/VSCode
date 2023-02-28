result = {}
count = 0
n = int(input())

for _ in range(n):
	number, judge = input().split()
	result[number] = judge

dabenzhong = []
for key, value in result.items():
	if value == "1":
		dabenzhong.append(key)
		count += 1

print(*dabenzhong)
print(f"There are {count} suspects.") if count > 1 else print("Da Ben Zhong is found!")