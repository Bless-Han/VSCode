# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> list[int]:
        return self.reversePrint(head.next) + [head.val] if head else []


a = ListNode(1)
b = ListNode(3)
c = ListNode(9)
a.next = b
b.next = c
s = Solution()

print(s.reversePrint(a))
