def is_prime(n):
    if n == 0 or n == 1:
        return False
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
    while radix_str:
        ret += int(radix_str[-1]) * (d**zhishu)
        radix_str = radix_str[:-1]
        zhishu += 1
    return ret


def main():
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

def to_base_d(num, d):
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        num, rem = divmod(num, d)
        result = str(rem) + result
    return result

def from_base_d(num, d):
    result = 0
    for digit in num:
        result = result * d + int(digit)
    return result


print(from_base_d("1001001", 2))
