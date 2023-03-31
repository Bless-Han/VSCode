'''
   @pintia psid=15 pid=711 compiler=PYTHON3
   
   ProblemSet: 数据结构与算法题目集（中文）
   
   Title: 7-3 树的同构
   
   https://pintia.cn/problem-sets/15/exam/problems/711
   
'''
# @pintia code=start
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

def isomorphic(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data != root2.data:
        return False
    return (isomorphic(root1.left, root2.left) and isomorphic(root1.right, root2.right))\
            or (isomorphic(root1.left, root2.right) and isomorphic(root1.right, root2.left))

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



# Path: test/temp.py

# @pintia code=end