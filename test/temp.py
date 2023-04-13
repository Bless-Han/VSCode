# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        if head.next is None:
            return True
        if head.next.next is None:
            return head.val == head.next.val
        
        # find the middle
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half
        prev = None
        curr = slow
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # compare the first half and the second half
        first = head
        second = prev
        while second is not None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True