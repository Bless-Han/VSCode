n = 0
passengers = []
passengers_count = []
index = [0,0]



# reutrn True if all of the passengers equal -1
def judge(passengers):
	for x in passengers:
		if x != -1:
			return False
	return True


# return the average of the sum
def ave_count(passengers_count):
	return sum(passengers_count) / len(passengers_count)


# return the minutes of the time people wating
# index[0] is the index of the bag
# index[1] is the index of the person
def wating(index):
	ret = 0
	while True:
		if index[1] >= n:
			index[1] %= n
		if passengers[index[1]] != -1:
			ret += 1
			if passengers[index[1]] == index[0]:
				passengers_count[index[1]] += ret
				passengers[index[1]] = -1
				break
		index[1] += 1

	for k in range(n):
		if passengers[k] != -1:
			passengers_count[k] += ret
	return ret



n = int(input())
temp = input().split()

for i in range(len(temp)):
	passengers.append(int(temp[i]))
	passengers_count.append(0)


# index is the nubmer of bag which on the machine
minutes = 0
# i is the index of the bag of now
for i in range(1, n + 1):
	index[0] = i;
	minutes += wating(index)




print(f"{minutes} {ave_count(passengers_count)}", end="")