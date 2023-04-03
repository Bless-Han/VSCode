class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

def isIdentical(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    return root1.data == root2.data and\
        isIdentical(root1.left, root2.left) and\
        isIdentical(root1.right, root2.right)

def main():
    while True:
        try:
            n, l = map(int, input().split())
            print("Ok")
        except Exception:
            break
        else:
            preOrder = map(int, input().split())
            root = None
            for data in preOrder:
                insert(root, data)
            for _ in range(l):
                preOrder = map(int, input().split())
                root2 = None
                for data in preOrder:
                    insert(root2, data)
                if isIdentical(root, root2):
                    print("Yes")
                else:
                    print("No")

if __name__ == "__main__":
    main()

