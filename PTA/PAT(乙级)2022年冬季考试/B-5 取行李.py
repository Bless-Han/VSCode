n = int(input())
passengers = list(map(int, input().split()))

# 总人数
numbers = len(passengers)
# 总耗时
count = 0

bags = []
for i in range(1, numbers+1):
	bags.append(i)

passengers_index = 0
while len(bags) != 0:
	for bag in bags:
		while len(passengers) > 0:
			count += 1
			if bag == passengers[passengers_index]:
				passengers.remove(bag)
				bags.remove(bag)
				print("-----------", count, bag, passengers[passengers_index])
				break
			passengers_index += 1
			passengers_index %= len(passengers)

print(count, count / numbers)
