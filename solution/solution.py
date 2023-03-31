class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def get_tree(n):
    t = []
    for _ in range(number):
        t.append(Node())
    for node in t:
        v, l, r = input().split()
        node.value = v
        if l == "-":
            node.left = None
        else:
            node.left = t[int(l)]
        if r == "-":
            node.right = None
        else:
            node.right = t[int(r)]
    return t


def print_t(t):
    for node in t:
        print(node.value, "", end="")
        if node.left:
            print(node.left.value, "", end="")
        else:
            print("None", "", end="")
        if node.right:
            print(node.right.value)
        else:
            print("None")

number = int(input())
t1 = get_tree(number)
number = int(input())
t2 = get_tree(number)

a = 20
a

print_t(t1)

print("Yes") if t1 == t2 else print("No")
