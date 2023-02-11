a = [1, 2, 3, 4]
for i1, v1 in enumerate(a):
	for i2, v2 in enumerate(a[i1 + 1:]):
		for i3, v3 in enumerate(a[i2 + 2:]):
			print("i1:", v1)
			print("i2:", v2)
			print("i3:", v3)
		print("-" * 20)
