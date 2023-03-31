class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

def isomorphic(root1, root2):
    if roo1 == None and root2 == None:
        return True
    if roo1 == None or root2 == None:
        return False
    if root1.data != root2.data:
        return False
    return isomorphic


def build_tree():
    n = int(input())
    if n == 0:
        return None
    nodes = []
    for i in range(n):
        nodes.append(Node(0))
    for i in range(n):
        data, left, right = input().split()
        nodes[i].data = data
        if left != '-':
            nodes[i].left = nodes[int(left)]
            nodes[int(left)].parent = nodes[i]
        if right != '-':
            nodes[i].right = nodes[int(right)]
            nodes[int(right)].parent = nodes[i]
    return get_root(nodes)

def get_root(nodes):
    for node in nodes:
        if node.parent == None:
            return node

if __name__ == '__main__':
    root1 = build_tree()
    root2 = build_tree()
    if isomorphic(root1, root2):
        print('Yes')
    else:
        print('No')


