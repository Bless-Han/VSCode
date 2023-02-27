import sys
a, b = map(int, input().split())

for n in range(b, a - 1, -1):
	for m in range(n, a - 1, -1):
		if (n**2 - m*n - m**2)**2 == 1:
			print(f"max( {m}^2 + {n}^2 ) = {m**2 + n**2}")
			sys.exit()

