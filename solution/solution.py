"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        # insert Node after every node
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = curr.next.next
        # assign random to new Node
        curr = head
        while curr:
            new = curr.next
            if curr.random:
                new.random = curr.random.next
            curr = curr.next.next
        # split old and new
        curr = head
        copy_head = curr.next
        while curr:
            copy = curr.next
            curr.next = curr.next.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        return copy_head
print("OK")
