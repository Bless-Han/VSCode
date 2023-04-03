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

def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return root1.data == root2.data and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)

def main():
    while True:
        try:
            n, m = map(int, input().split())
        except Exception:
            break
            if n == 0:
                break
            preOrder = list(map(int, input().split()))
            root = None
            for data in preOrder:
                root = insert(root, data)
            for i in range(m):
                temp = list(map(int, input().split()))
                root2 = None
                for data in temp:
                    root2 = insert(root2, data)
                if isIdentical(root, root2):
                    print('Yes')
                else:
                    print('No')

if __name__ == '__main__':
    main()

# @pintia code=end