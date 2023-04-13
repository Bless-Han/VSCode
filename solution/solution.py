def check(s):
    try:
        left_A, right = s.split("P")
        middle_A, right_A = right.split("T")
    except Exception:
        return False
    else:
        if not full_A(left_A) or not full_A(middle_A) or not full_A(right_A):
            return False
        if len(middle_A) == 0:
            return False
        return len(left_A) * len(middle_A) == len(right_A)

def full_A(s):
    for c in s:
        if c != "A":
            return False
    return True

n = int(input())
for _ in range(n):
    print("YES") if check(input()) else print("NO")
