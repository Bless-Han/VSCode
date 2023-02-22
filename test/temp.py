my_list = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, my_list)
squares_tuple = ("Neo", 20, 100)
squares_set = {2, 1, 3, 9, 1, "Neo", "Good", "Neo"}
squares_tuple = ("Neo", 10, 100)

print(squares_tuple[0])  # 输出 (1, 4, 9, 16, 25)
print(squares_set)  # 输出 {1, 4, 9, 16, 25}
