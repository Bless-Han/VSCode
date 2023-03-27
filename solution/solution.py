import bisect

my_list = [1, 3, 4, 5, 7, 9, 11]

index = bisect.bisect_left(my_list, 8)
print(index)
