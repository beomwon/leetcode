# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        check = []
        while True:
            try:
                if head.next == -1:
                    return False
                if head.next in check:
                    return True
                check.append(head)
                head = head.next
            except:
                return False
            
            