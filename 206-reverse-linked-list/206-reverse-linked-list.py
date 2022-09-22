# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        next_ = cur = before = head
        while cur.next:
            next_ = cur.next
            cur.next = before
            before = cur
            cur = next_
        cur.next = before
        head.next = None
        
        return cur
            
            