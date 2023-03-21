
class Cursor:
    x = 0
    y = 0

s = input()
row_count = len(s) // 3
ver_count = len(s) - row_count * 2

result = [list(" " * ver_count)] * (row_count + 1)

curr = Cursor()
for c in s:
    result[curr.x][curr.y] = c
    print(result[curr.x][curr.y], curr.x, curr.y, c)
    if curr.x < row_count and curr.y == 0:
        curr.x += 1

for row in result:
    print(row)
for row in result:
    print("".join(row))
