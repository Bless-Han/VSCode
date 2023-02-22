my_list = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, my_list)
squares_tuple = tuple(squares)
squares_set = set(squares)

print(squares_tuple)  # 输出 (1, 4, 9, 16, 25)
print(squares_set)  # 输出 {1, 4, 9, 16, 25}
