'''
   @pintia psid=15 pid=712 compiler=PYTHON3
   
   ProblemSet: 数据结构与算法题目集（中文）
   
   Title: 7-4 是否同一棵二叉搜索树
   
   https://pintia.cn/problem-sets/15/exam/problems/712
   
'''
# @pintia code=start
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def isSameBST(preOrder, inOrder):
    if len(preOrder) == 0:
        return True
    if len(preOrder) == 1:
        return preOrder[0] == inOrder[0]
    root = preOrder[0]
    rootIndex = inOrder.index(root)
    leftInOrder = inOrder[:rootIndex]
    rightInOrder = inOrder[rootIndex+1:]
    leftPreOrder = preOrder[1:rootIndex+1]
    rightPreOrder = preOrder[rootIndex+1:]
    return isSameBST(leftPreOrder, leftInOrder) and isSameBST(rightPreOrder, rightInOrder)

def main():
    while True:
        n, m = map(int, input().split())
        if n == 0:
            break
        preOrder = list(map(int, input().split()))
        inOrder = sorted(preOrder)
        for i in range(m):
            temp = list(map(int, input().split()))
            if isSameBST(temp, inOrder):
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()

# @pintia code=end