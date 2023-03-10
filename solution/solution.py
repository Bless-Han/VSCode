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
        nodes = []
        curr = head
        while curr:
            nodes.append(copy.deepcopy(curr))
            curr = curr.next
        prev = nodes[0]
        for node in nodes[1:]:
            prev.next = node
            prev.random = random.choice(nodes)
            prev = node

        return nodes[0]



print("OK")
