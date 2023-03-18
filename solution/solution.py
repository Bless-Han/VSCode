import sys

primes = {2}
def is_prime(n):
    for prime in primes:
        if n % prime == 0:
            return False
    return True

for x in range(2, 10**4+1):
    if is_prime(x):
        primes.add(x)

final = []
for i in range(10**4):
    final.append(-1)

n = int(input())
for i in range(1, n + 1):
    final[int(sys.stdin.readline().strip())] = i

k = int(input())
for_checked = set()
for _ in range(k):
    search = int(sys.stdin.readline().strip())
    print(f"{search:04}", end=": ")

    try:
        paiming = final[search]
    except ValueError:
        print("Are you kidding?")
    else:
        if paiming == -1:
            print("Are you kidding?")
            continue

        if search in for_checked:
            print("Checked")
            continue
        else:
            for_checked.add(search)

        if paiming == 1:
            print("Mystery Award")
        elif paiming in primes:
            print("Minion")
        else:
            print("Chocolate")


print(7 / 18)

print(5 / 12)

print(7 / 12)
print(13 / 20)
