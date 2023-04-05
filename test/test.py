class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_same(r1, r2):
    if r1 == None and r2 == None:
        return True
    if r1 == None or r2 == None:
        return False
    return r1.data == r2.dara and is_same(r1.left, r2.left) and is_same(r1.right, r2.right)

def build_tree(r, data):
    if not r:
        return Node(data)


try:
    while True:
        n, l = map(int, input().split())
        r1 = None
        numbers = map(int, input().split())
        for number in numbers:
            r1 = build_tree(r1, number)
        for _ in range(l):
            numbers = map(int, input().split())
            for number in nubmers:
                r2 = build_tree(r2, number)
        print("Yes") if is_same(r1, r2) else print("No")
except Exception:
    ...
