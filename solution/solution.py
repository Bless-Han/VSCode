def is_prime(n):
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

def change_radix(n, d):
    radix_str = ""
    while n:
        radix_str += str(n%d)
        n //= d
    ret = 0
    zhishu = 0
    print(n, radix_str, ret)
    while radix_str:
        ret += int(radix_str[-1]) * (d**zhishu)
        radix_str = radix_str[:-1]
        zhishu += 1
    print(n, radix_str, ret)
    return ret


while True:
    try:
        n, d = map(int, input().split())
    except ValueError:
        break
    if n < 0:
        break
    if is_prime(n) and is_prime(change_radix(n, d)):
        print("Yes")
    else:
        print("No")

