board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for col in zip(*board):
    print(col)
