n = int(input())
people = []
for i in range(n):
	temp = input().split()
	number = int(temp[0])
	judge = int(temp[1])
	if number in people:
		people[number] = judge
	else:
		people.append({number: judge})



print(people)

dabenzhong = 0


