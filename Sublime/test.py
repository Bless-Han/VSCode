
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = 33
ans = 1
for i in range(0, 6):
	ans *= n
ans *= 16

print(ans)
print(200 / 13)
