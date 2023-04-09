# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while fast != None and slow != fast:
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
            slow = slow.next
        if fast == None:
            return False
        else:
            return True

print()
