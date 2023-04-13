# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(l1.val + l2.val)
        l1 = l1.next
        l2 = l2.next
        curr = head
        while l1 and l2:
            curr.next = ListNode(l1.val + l2.val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            curr.next = ListNode(l1.val)
            curr = curr.next
            l1 = l1.next
        while l2:
            curr.next = ListNode(l2.val)
            curr = curr.next
            l2 = l2.next
        curr.next = None

        curr = head
        jinwei = 0
        if curr.val >= 10:
            jinwei = curr.val // 10
            curr.val %= 10
            curr = curr.next
        while curr:
            if jinwei:
                curr.val += jinwei
                jinwei = 0
            if curr.val >= 10:
                jinwei = curr.val // 10
                curr.val %= 10
            curr = curr.next
        curr = head
        while curr.next:
            curr = curr.next
        if jinwei:
            curr.next = ListNode(jinwei)
            jinwei = 0

        # reverse
        # curr = head
        # head = None
        # while curr:
            # temp = curr.next
            # curr.next = head
            # head = curr
            # curr = temp

        return head
