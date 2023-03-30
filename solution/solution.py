class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def print_t(t):
    for node in t:
        print(node.value, node.left, node.right)

number = int(input())
t1 = [Node() * number]
for _ in range(number):
    value, left, right = input().split()
    t1.append(Node(value, left, right))
number = int(input())
t2 = []
for _ in range(number):
    value, left, right = input().split()
    t2.append(Node(value, left, right))

print("Yes") if t1 == t2 else print("No")
