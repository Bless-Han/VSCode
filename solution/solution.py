# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    import copy
    import random
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # 把链接添加到list里
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        # 求random_index
        random_index = []
        for node in nodes:
            if node.random:
                random_index = nodes.index(node.random)
            else:
                random_index = -1

        # copy nodes to new_nodes
        new_nodes = copy.deepcopy(nodes)
        prev = new_nodes[0]
        for i in range(1, len(new_nodes)):
            prev.next = new_nodes[i]
            if random_index[i] == -1
                prev.random = None
            else:
                prev.random = new_nodes[random_index[i]]
            prev = prev.next

        return new_nodes[0]



    print("OK")
