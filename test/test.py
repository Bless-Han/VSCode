# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not head B:
            return None
        curA = headA
        while curA.next:
            curA = curA.next
        curB = headB
        while curB.next:
            curB = curB.next
        if curA != curB:
            return None
        else:
        curA = headA
        curB = headB


print()
