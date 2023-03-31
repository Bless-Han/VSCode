'''
树的同构
分数 25   提交人数 27857   通过人数 7343   通过率 26.36%
作者 陈越     单位 浙江大学
给定两棵树T1和T2。如果T1可以通过若干次左右孩子互换就变成T2，则我们称两棵树是“同构”的。例如图1给出的两棵树就是同构的，因为我们把其中一棵树的结点A、B、G的左右孩子互换后，就得到另外一棵树。而图2就不是同构的。

fig1.jpg
图1

图2
现给定两棵树，请你判断它们是否是同构的。

输入格式:
输入给出2棵二叉树树的信息。对于每棵树，首先在一行中给出一个非负整数NN (\le 10≤10)，即该树的结点数（此时假设结点从0到N-1N−1编号）；随后NN行，第ii行对应编号第ii个结点，给出该结点中存储的1个英文大写字母、其左孩子结点的编号、右孩子结点的编号。如果孩子结点为空，则在相应位置上给出“-”。给出的数据间用一个空格分隔。注意：题目保证每个结点中存储的字母是不同的。

输出格式:
如果两棵树是同构的，输出“Yes”，否则输出“No”。

输入样例1（对应图1）：
8
A 1 2
B 3 4
C 5 -
D - -
E 6 -
G 7 -
F - -
H - -
8
G - 4
B 7 6
F - -
A 5 1
H - -
C 0 -
D - -
E 2 -
输出样例1:
Yes
输入样例2（对应图2）：
8
B 5 7
F - -
A 0 3
C 6 -
H - -
D - -
G 4 -
E 1 -
8
D 6 -
B 5 -
E - -
H - -
C 0 2
G - 3
F - -
A 1 4
输出样例2:
No
'''
# Q: 可以帮助我解决这道算法问题吗？
# A: 可以，我会尽力帮助你解决这道算法问题。

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

# Q: 请问这个函数的名字来自哪里?
# A: 这个函数的名字来自于“同构”这个词的英文isomorphic。
# Q: 谢谢你的解答
# A: 不客气。
def isomorphic(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data != root2.data:
        return False
    return (isomorphic(root1.left, root2.left) and isomorphic(root1.right, root2.right)) or (isomorphic(root1.left, root2.right) and isomorphic(root1.right, root2.left))

def build_tree():
    n = int(input())
    if n == 0:
        return None
    nodes = []
    for i in range(n):
        nodes.append(Node(i))
    for i in range(n):
        data, left, right = input().split()
        nodes[i].data = data
        if left != '-':
            nodes[i].left = nodes[int(left)]
        if right != '-':
            nodes[i].right = nodes[int(right)]
    return get_root(nodes)

# 返回nodes中的根节点
def get_root(nodes):
    for node in nodes:
        if node.left is None and node.right is None:
            continue
        if node.left is not None:
            node.left.parent = node
        if node.right is not None:
            node.right.parent = node
    for node in nodes:
        if node.parent is None:
            return node

if __name__ == '__main__':
    root1 = build_tree()
    root2 = build_tree()
    if isomorphic(root1, root2):
        print('Yes')
    else:
        print('No')

# Path: test/temp.py

# Q: Thank you for help me solve this problem.
# A: You are welcome.