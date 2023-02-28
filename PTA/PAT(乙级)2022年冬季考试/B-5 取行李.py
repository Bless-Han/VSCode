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

p_index = 0
for bag in bags:
	while len(passengers) > 0:
		count += 1
		whole_count += len(passengers)
		if bag == passengers[p_index]:
			passengers.remove(bag)
			if len(passengers) != 0:
				p_index %= len(passengers)
			break
		p_index += 1
		p_index %= len(passengers)

print(count, whole_count / numbers)
