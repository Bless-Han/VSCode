n = int(input())
passengers = list(map(int, input().split()))

# 总人数
numbers = len(passengers)
# 所有人耗时
whole_count = 0
# 机器耗时
count = 0

bags = []
for i in range(1, numbers+1):
	bags.append(i)

passengers_index = 0
for bag in bags:
	while True:
		count += 1
		if bag == passengers[passengers_index]:
			print("-----------", count, bag, passengers[passengers_index])
			passengers.remove(bag)
			bags.remove(bag)
			break
		passengers_index += 1
		passengers_index %= len(passengers)

print(count, count / numbers)
