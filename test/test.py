class Node:
    def __init__(self, d):
        self.d = d
        self.l = None
        self.r = None

def isIdentical(r1, r2):
    if not r1 and not r2:
        return True
    if not r1 or not r2:
        return False
    return r1.d == r2.d and isIdentical(r1.l, r2.l) and isIdentical(r1.r, r2.r)

def insert(r, d):
    if not r:
        return Node(d)
    if d < r.d:
        r.l = insert(r.l, d)
    else:
        r.r = insert(r.r, d)
    return r

while True:
    try:
        n, l = map(int, input().split())
    except Exception:
        break
    else:
        nums = map(int, input().split())
        r1 = None
        for num in nums:
            r1 = insert(r1, num)
        for _ in range(l):
            nums = map(int, input().split())
            r2 = None
            for num in nums:
                r2 = insert(r2, num)
            print("Yes") if isIdentical(r1, r2) else print("No")

