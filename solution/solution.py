# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: 'Node') -> 'Node':
        import copy
        import random
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
        for i in range(len(nodes)):
            if nodes[i].random:
                random_index.append(nodes.index(nodes[i].random))
            else:
                random_index.append(-1)

        # copy nodes to new_nodes
        new_nodes = copy.deepcopy(nodes)
        # To link
        prev = new_nodes[0]
        for i in range(1, len(new_nodes)):
            prev.next = new_nodes[i]
            prev = prev.next

        # count random_index
        for i in range(len(new_nodes)):
            if random_index[i] == -1:
                new_nodes[i].random = None
            else:
                new_nodes[i].random = new_nodes[random_index[i]]

        return new_nodes[0]


