def is_prime(n):
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True


primes = []
n = int(input())

final = []
for _ in range(n):
    final.append(input())

k = int(input())
for_checked = []
for _ in range(k):
    search = input()
    print(search, end=": ")

    try:
        ind = final.index(search)
    except ValueError:
        print("Are you kidding?")
    else:
        if search in for_checked:
            print("Checked")
            continue
        else:
            for_checked.append(search)
        if ind == 0:
            print("Mystery Award")
        elif (ind+1) in primes:
            print("Minion")
        else:
            print("Chocolate")

