'''
是否同一棵二叉搜索树:

给定一个插入序列就可以唯一确定一棵二叉搜索树。然而，一棵给定的二叉搜索树却可以由多种不同的插入序列得到。例如分别按照序列{2, 1, 3}和{2, 3, 1}插入初始为空的二叉搜索树，都得到一样的结果。于是对于输入的各种插入序列，你需要判断它们是否能生成一样的二叉搜索树。

输入格式:
输入包含若干组测试数据。每组数据的第1行给出两个正整数NN (\le 10≤10)和LL，分别是每个序列插入元素的个数和需要检查的序列个数。第2行给出NN个以空格分隔的正整数，作为初始插入序列。随后LL行，每行给出NN个插入的元素，属于LL个需要检查的序列。

简单起见，我们保证每个插入序列都是1到NN的一个排列。当读到NN为0时，标志输入结束，这组数据不要处理。 输出格式: 对每一组需要检查的序列，如果其生成的二叉搜索树跟对应的初始序列生成的一样，输出“Yes”，否则输出“No”。

输入样例:
4 2
3 1 4 2
3 4 1 2
3 2 4 1
2 1
2 1
1 2
0
输出样例:
Yes
No
No
'''

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
        except Exception:
            break

if __name__ == '__main__':
    main()