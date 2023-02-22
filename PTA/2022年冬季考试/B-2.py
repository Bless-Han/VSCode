s = input().split()
a = int(s[0])
b = int(s[1])

numbers = []
for i in range(0, a):
	numbers.append(0)
for i in range(a, b + 1):
	numbers.append(i ** 2)

m, n = 0, 0
for i in range(a, b + 1):
	for j in range(i, b + 1):
		if numbers[j] - i * j - numbers[i] == 1:
			n = i
			m = j

print(f"max( {n}^2 + {m}^2 ) = {n ** 2 + m ** 2}", end="")