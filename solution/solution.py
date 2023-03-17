'''
ERROR: aaa is not a legal number

ERROR: 2.3.4 is not a legal number
ERROR: 7.123 is not a legal number
The average of 3 numbers is 1.38
'''

lksfjldksjl = input()
numbers_s = input().split()

# lists for numbers
lists = []
for number in numbers_s:
    try:
        number = float(number)
    except ValueError:
        print(f"ERROR: {number} is not a legal number")
    else:
        if -1000 <= number <= 1000 and number - round(number, 2) == 0:
            lists.append(number)
        else:
            print(f"ERROR: {number} is not a legal number")

if len(lists) == 0:
    print("The average of 0 numbers is Undefined")
elif len(lists) == 1:
    print(f"The average of 1 number is {lists[1]}")
else:
    print(f"The average of {len(lists)} numbers is {sum(lists) / len(lists):.2f}")

