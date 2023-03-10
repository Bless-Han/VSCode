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
            random_index = nodes.index(node.random)

        # copy nodes to new_nodes 并计算next and random
        new_nodes = copy.deepcopy(nodes)
        node = [0]
        for node in new_nodes[1:]:


        return new_nodes[0]



print("OK")
