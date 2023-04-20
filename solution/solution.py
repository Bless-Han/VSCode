
def isomorphic(r1, r2):
    if not r1 and not r2:
        return True
    if not r1 or not r2:
        return False
    return r1.val == r2.val and \
            (
            (isomorphic(r1.left, r2.left and isomorphic(r1.right, r2.right))) or\
            (isomorphic(r1.left, r2.right and isomorphic(r1.right, r2.left)))
            )

def build_tree():
    n = int(input())
    nodes = []
    for _ in range(n):
        nodes.append(Node())
    for i in range(n):
        val, left, right = input().split()
        nodes[i].val = val
        if left != '-':
            # TODO:
            ...
    return r

