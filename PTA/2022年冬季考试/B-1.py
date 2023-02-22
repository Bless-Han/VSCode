zs = "(zhangsheng)"
def get_times(s):
	times = 0
	for i in range(len(s) - 12):
		if s[i:i + 12] == zs:
			times += 1
	return times











suppose = int(input())
s = input()
# s = "Hello (zhangsheng).  Glad to meet everyone(zhang sheng). Let me hear your zhangsheng! #"
while s[-1] != '#':
	s += input()

times = get_times(s)

if times >= suppose:
	print(f"{times} True")
else:
	print(f"{times} False")

